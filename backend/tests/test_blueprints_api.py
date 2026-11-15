from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_blueprint():
    response = client.post(
        "/blueprints",
        json={
            "business_description": (
                "We need an AI agent to answer customer questions."
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Customer Support Automation"


def test_short_description_returns_422():
    response = client.post(
        "/blueprints",
        json={"business_description": "short"},
    )

    assert response.status_code == 422