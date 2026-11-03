from fastapi.testclient import TestClient
from backend.main import app

def test_health_pipeline_loaded():
  
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "model_loaded": True
    }

def test_health_endpoint():
 
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
