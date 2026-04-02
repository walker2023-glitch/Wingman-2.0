from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_dates():
    response = client.get("/api/dates")
    assert response.status_code == 200

def test_prediction_logic():
    # Test your R-model math: 5 interests, 10 hours, 3 days notice, 1 person
    response = client.post("/api/predict", json={"interests": 5, "hours": 10, "notice": 3, "people": 1})
    assert response.status_code == 200
    assert "chance" in response.json()
