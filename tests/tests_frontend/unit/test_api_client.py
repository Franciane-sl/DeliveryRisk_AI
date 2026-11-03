from unittest.mock import Mock, patch
import pytest
import requests
from frontend.api_client import APIClient, APIClientError


@pytest.fixture
def client():
    return APIClient(
        base_url="http://localhost:8000",
        timeout=10,
    )


@pytest.fixture
def successful_response():
    response = Mock()
    response.ok = True
    response.status_code = 200
    response.json.return_value = {"status": "healthy"}
    return response


def test_get_health(client, successful_response):
    with patch(
        "frontend.api_client.requests.request",
        return_value=successful_response,
    ) as mock_request:

        result = client.get_health()

    assert result == {"status": "healthy"}
    mock_request.assert_called_once_with(
        method="GET",
        url="http://localhost:8000/health",
        timeout=10,
    )


def test_predict(client, successful_response):
    payload = {"quantidade_itens": 2}

    with patch(
        "frontend.api_client.requests.request",
        return_value=successful_response,
    ) as mock_request:

        result = client.predict(payload)

    assert result == {"status": "healthy"}
    mock_request.assert_called_once_with(
        method="POST",
        url="http://localhost:8000/predict",
        timeout=10,
        json=payload,
    )


def test_get_predictions(client, successful_response):
    successful_response.json.return_value = []

    with patch(
        "frontend.api_client.requests.request",
        return_value=successful_response,
    ):
        result = client.get_predictions()

    assert result == []


def test_get_prediction(client, successful_response):
    with patch(
        "frontend.api_client.requests.request",
        return_value=successful_response,
    ) as mock_request:

        result = client.get_prediction(10)

    assert result == {"status": "healthy"}
    assert mock_request.call_args.kwargs["url"].endswith(
        "/predictions/10"
    )


def test_delete_prediction(client):
    response = Mock()
    response.ok = True
    response.status_code = 204

    with patch(
        "frontend.api_client.requests.request",
        return_value=response,
    ):
        result = client.delete_prediction(10)

    assert result is None


def test_get_metrics(client, successful_response):
    successful_response.json.return_value = {
        "projeto": "DeliveryRisk AI"
    }

    with patch(
        "frontend.api_client.requests.request",
        return_value=successful_response,
    ):
        result = client.get_metrics()

    assert result["projeto"] == "DeliveryRisk AI"


def test_timeout(client):
    with patch(
        "frontend.api_client.requests.request",
        side_effect=requests.exceptions.Timeout,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert "demorou para responder" in exc_info.value.message
    assert exc_info.value.status_code is None


def test_connection_error(client):
    with patch(
        "frontend.api_client.requests.request",
        side_effect=requests.exceptions.ConnectionError,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert "Não foi possível conectar" in exc_info.value.message


def test_generic_request_error(client):
    with patch(
        "frontend.api_client.requests.request",
        side_effect=requests.exceptions.RequestException,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert "erro na comunicação" in exc_info.value.message

def test_http_error_with_message(client):
    response = Mock()
    response.ok = False
    response.status_code = 404
    response.json.return_value = {
        "error": "Not Found",
        "message": "Previsão não encontrada.",
    }

    with patch(
        "frontend.api_client.requests.request",
        return_value=response,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_prediction(999)

    assert exc_info.value.message == "Previsão não encontrada."
    assert exc_info.value.status_code == 404


def test_http_error_without_message(client):
    response = Mock()
    response.ok = False
    response.status_code = 500
    response.json.return_value = {
        "error": "Internal Server Error"
    }

    with patch(
        "frontend.api_client.requests.request",
        return_value=response,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert (
        exc_info.value.message
        == "Não foi possível processar a solicitação."
    )
    assert exc_info.value.status_code == 500


def test_http_error_with_invalid_json(client):
    response = Mock()
    response.ok = False
    response.status_code = 500
    response.json.side_effect = ValueError

    with patch(
        "frontend.api_client.requests.request",
        return_value=response,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert (
        exc_info.value.message
        == "A API retornou uma resposta de erro inválida."
    )
    assert exc_info.value.status_code == 500

def test_invalid_json_response(client):
    response = Mock()
    response.ok = True
    response.status_code = 200
    response.json.side_effect = ValueError

    with patch(
        "frontend.api_client.requests.request",
        return_value=response,
    ):
        with pytest.raises(APIClientError) as exc_info:
            client.get_health()

    assert (
        exc_info.value.message
        == "A API retornou uma resposta JSON inválida."
    )
    assert exc_info.value.status_code == 200
