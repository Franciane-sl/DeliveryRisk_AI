import pytest

from frontend.utils.validators import validate_prediction_data


@pytest.fixture
def dados_validos():
    return {
        "quantidade_itens": 2,
        "valor_total_produtos": 150.0,
        "customer_state": "SP",
        "seller_state_mais_frequente": "RJ",
        "customer_city": "São Paulo",
    }


class TestValidatePredictionData:

    def test_dados_validos(self, dados_validos):
        assert validate_prediction_data(dados_validos) == []

    def test_campo_none(self, dados_validos):
        dados_validos["customer_city"] = None

        resultado = validate_prediction_data(dados_validos)

        assert (
            "Preencha todos os campos antes de gerar a previsão."
            in resultado
        )

    def test_campo_string_vazia(self, dados_validos):
        dados_validos["customer_city"] = ""

        resultado = validate_prediction_data(dados_validos)

        assert (
            "Preencha todos os campos antes de gerar a previsão."
            in resultado
        )

    def test_varios_campos_obrigatorios_vazios(self, dados_validos):
        dados_validos["customer_city"] = ""
        dados_validos["quantidade_itens"] = None

        resultado = validate_prediction_data(dados_validos)

        assert len(resultado) == 1
        assert (
            "Preencha todos os campos antes de gerar a previsão."
            in resultado
        )

    @pytest.mark.parametrize(
        "estado",
        ["S", "SPP", "123", "", "S1"],
    )
    def test_sigla_estado_invalida_customer_state(
        self, dados_validos, estado
    ):
        dados_validos["customer_state"] = estado

        resultado = validate_prediction_data(dados_validos)

        assert (
            "Informe as siglas dos estados com exatamente duas letras."
            in resultado
        )

    @pytest.mark.parametrize(
        "estado",
        ["R", "RJJ", "123", "", "R1"],
    )
    def test_sigla_estado_invalida_seller_state(
        self, dados_validos, estado
    ):
        dados_validos["seller_state_mais_frequente"] = estado

        resultado = validate_prediction_data(dados_validos)

        assert (
            "Informe as siglas dos estados com exatamente duas letras."
            in resultado
        )

    def test_siglas_minusculas_validas(self, dados_validos):
        dados_validos["customer_state"] = "sp"
        dados_validos["seller_state_mais_frequente"] = "rj"

        assert validate_prediction_data(dados_validos) == []

    def test_dois_estados_invalidos(self, dados_validos):
        dados_validos["customer_state"] = "S"
        dados_validos["seller_state_mais_frequente"] = "RJ1"

        resultado = validate_prediction_data(dados_validos)

        assert len(resultado) == 1
        assert (
            "Informe as siglas dos estados com exatamente duas letras."
            in resultado
        )

    def test_campos_obrigatorios_e_estados_invalidos(
        self, dados_validos
    ):
        dados_validos["customer_city"] = ""
        dados_validos["customer_state"] = "S"

        resultado = validate_prediction_data(dados_validos)

        assert len(resultado) == 2
