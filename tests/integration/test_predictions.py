import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from backend.main import app
from backend.dependencies import get_pipeline
import backend.database.connection as db_connection
from backend.database.models import create_predictions_table
from tests.conftest import create_valid_payload


def test_create_prediction(client):
    payload = create_valid_payload()

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction_id"] > 0
    assert data["prediction"] == 1
    assert data["prediction_label"] == "Atraso previsto"
    assert data["delay_probability"] == 0.80
    assert data["message"] == "Previsão realizada e salva no histórico."
