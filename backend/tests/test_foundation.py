import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.main import app

client = TestClient(app)


def test_health_check_returns_200_and_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_cors_preflight():
    response = client.options(
        "/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"


def test_get_db_session_lifecycle():
    generator = get_db()
    db = next(generator)

    assert isinstance(db, Session)

    with pytest.raises(StopIteration):
        next(generator)