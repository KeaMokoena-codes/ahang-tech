import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Local SQLite fallback; supports DATABASE_URL for Postgres in staging/production
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ahangtech.db")

# SQLite requires check_same_thread=False for multi-threaded FastAPI requests
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Dependency that yields a database session and ensures clean teardown."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()