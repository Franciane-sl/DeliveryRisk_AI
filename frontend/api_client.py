import requests
from frontend.config import API_BASE_URL

# Define a classe de exceção personalizada para erros da API
class APIClientError(Exception):

    def __init__(self, message: str, status_code: int | None = None):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

# Define a classe de cliente da API para interagir com os endpoints
class APIClient:

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        timeout: int = 10,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs,
            )

        except requests.exceptions.Timeout as exc:
            raise APIClientError(
                "A API demorou para responder. Tente novamente."
            ) from exc

        except requests.exceptions.ConnectionError as exc:
            raise APIClientError(
                "Não foi possível conectar à API. "
                "Verifique se o servidor está em execução."
            ) from exc

        except requests.exceptions.RequestException as exc:
            raise APIClientError(
                "Ocorreu um erro na comunicação com a API."
            ) from exc

        if not response.ok:
            try:
                error_data = response.json()
                message = error_data.get(
                    "message",
                    "Não foi possível processar a solicitação.",
                )
            except ValueError:
                message = "A API retornou uma resposta de erro inválida."

            raise APIClientError(
                message=message,
                status_code=response.status_code,
            )

        if response.status_code == 204:
            return None

        try:
            return response.json()
        except ValueError as exc:
            raise APIClientError(
                "A API retornou uma resposta JSON inválida.",
                status_code=response.status_code,
            ) from exc

    def get_health(self) -> dict:
        return self._request("GET", "/health")

    def predict(self, data: dict) -> dict:
        return self._request(
            "POST",
            "/predict",
            json=data,
        )

    def get_predictions(self) -> list:
        return self._request("GET", "/predictions")

    def get_prediction(self, prediction_id: int) -> dict:
        return self._request(
            "GET",
            f"/predictions/{prediction_id}",
        )

    def delete_prediction(self, prediction_id: int) -> None:
        return self._request(
            "DELETE",
            f"/predictions/{prediction_id}",
        )

    def get_metrics(self) -> dict:
        return self._request("GET", "/metrics")
