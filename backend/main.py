import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AhangTech API",
    version="0.1.0",
    description="Decoupled ConTech API for Asset Management, Reporting, and Estimations.",
)

# Allowed frontend origins (configurable via FRONTEND_URL env var)
# Default addresses cover standard local Vite and local development servers
allowed_origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000",
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    summary="Health check",
)
def health_check() -> dict[str, str]:
    return {"status": "ok"}