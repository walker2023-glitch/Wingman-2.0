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

def test_create_and_read_date():
    # Try removing the '/api' prefix if your FastAPI isn't using a router
    new_date = {"name": "Porter's Craft", "description": "Burgers", "category": "Food", "budget": 15, "likes": 0}
    
    # CHANGE THIS LINE to match your actual @app.post route in main.py
    create_response = client.post("/dates", json=new_date) 
    
    assert create_response.status_code == 200
    # 2. Read it back to ensure it integrated with the DB
    read_response = client.get("/api/dates")
    assert any(d['name'] == "Porter's Craft" for d in read_response.json())
