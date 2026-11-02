from tests.conftest import create_valid_payload

def test_list_predictions(client):
    client.post("/predict", json=create_valid_payload())
    client.post("/predict", json=create_valid_payload())

    response = client.get("/predictions")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_prediction_by_id(client):
    create_response = client.post(
        "/predict",
        json=create_valid_payload()
    )

    prediction_id = create_response.json()["prediction_id"]

    response = client.get(f"/predictions/{prediction_id}")

    assert response.status_code == 200
    assert response.json()["id"] == prediction_id
    assert response.json()["prediction"] == 1


def test_get_prediction_not_found(client):
    response = client.get("/predictions/999")

    assert response.status_code == 404
    assert response.json()["error"] == "Not Found"
    assert response.json()["message"] == "Previsão não encontrada."


def test_delete_prediction(client):
    create_response = client.post(
        "/predict",
        json=create_valid_payload()
    )

    prediction_id = create_response.json()["prediction_id"]

    response = client.delete(f"/predictions/{prediction_id}")

    assert response.status_code == 204

    detail_response = client.get(f"/predictions/{prediction_id}")

    assert detail_response.status_code == 404


def test_delete_prediction_not_found(client):
    response = client.delete("/predictions/999")

    assert response.status_code == 404
    assert response.json()["error"] == "Not Found"
    assert response.json()["message"] == "Previsão não encontrada."
    

def test_history_saves_input_data(client):
    payload = create_valid_payload()

    client.post("/predict", json=payload)

    response = client.get("/predictions")

    assert response.status_code == 200
    assert response.json()[0]["input_data"] == payload
