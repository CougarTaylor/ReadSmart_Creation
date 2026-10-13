from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_running_status():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ReadSmart API is running"}


def test_prototype_response_accepts_section_and_response():
    response = client.post(
        "/prototype/response",
        json={
            "section": "The dog ran through the park.",
            "student_response": "The dog went to the park.",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "section_received": True,
        "response_received": True,
        "section_word_count": 6,
        "response_word_count": 6,
    }


def test_prototype_response_rejects_missing_field():
    response = client.post(
        "/prototype/response",
        json={"section": "The dog ran through the park."},
    )
    # 422 = FastAPI validation error: the request was the wrong shape.
    assert response.status_code == 422


def test_prototype_response_rejects_empty_text():
    response = client.post(
        "/prototype/response",
        json={"section": "", "student_response": "Something"},
    )
    assert response.status_code == 422
