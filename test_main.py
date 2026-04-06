import pytest
from fastapi.testclient import TestClient
from main import app
import models
from database import engine

client = TestClient(app)

# Create tables before running tests
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    models.Base.metadata.create_all(bind=engine)
    yield
    # Optional: models.Base.metadata.drop_all(bind=engine)

def test_read_dates():
    response = client.get("/api/dates")
    assert response.status_code == 200
    # We expect an empty list [] or a list of dates
    assert isinstance(response.json(), list)

def test_prediction_logic():
    payload = {"interests": 5, "hours": 10, "notice": 3, "people": 2}
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 200
    assert "chance" in response.json()

def test_date_features():
    # 1. Test the Success Predictor (Logistic Regression)
    predict_data = {"interests": 5, "hours": 2, "notice": 3, "people": 2}
    pred_res = client.post("/api/predict", json=predict_data)
    assert pred_res.status_code == 200
    assert "chance" in pred_res.json()

    # 2. Test getting the dates list
    get_res = client.get("/api/dates")
    assert get_res.status_code == 200
