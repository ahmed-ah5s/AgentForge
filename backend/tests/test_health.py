
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "app": "AgentForge",
        "version": "0.1.0",
    }


def test_cors_allows_frontend_origin():
    response = client.get(
        "/health",
        headers={"Origin": "http://localhost:3000"},
    )

    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"


def test_cors_blocks_unknown_origin():
    response = client.get(
        "/health",
        headers={"Origin": "http://evil.com"},
    )

    assert "access-control-allow-origin" not in response.headers
