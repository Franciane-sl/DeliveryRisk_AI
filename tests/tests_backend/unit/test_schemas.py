import pytest
from pydantic import ValidationError

from backend.schemas import PredictionInput, PredictionOutput


@pytest.fixture
def dados_validos():
    
    return {
        "quantidade_itens": 2,
        "quantidade_produtos_distintos": 2,
        "quantidade_vendedores_distintos": 1,
        "quantidade_categorias_distintas": 2,
        "quantidade_estados_vendedores_distintos": 1,
        "quantidade_cidades_vendedores_distintas": 1,
        "valor_total_produtos": 150.0,
        "frete_total": 25.0,
        "product_weight_g_medio": 500.0,
        "product_length_cm_medio": 20.0,
        "product_height_cm_medio": 10.0,
        "product_width_cm_medio": 15.0,
        "ano_compra": 2018,
        "mes_compra": 5,
        "dia_mes_compra": 15,
        "dia_semana_compra": 1,
        "hora_compra": 14,
        "customer_zip_code_prefix": 12345,
        "customer_city": "sao paulo",
        "customer_state": "SP",
        "categoria_produto_mais_frequente": "beleza_saude",
        "seller_state_mais_frequente": "SP",
        "seller_city_mais_frequente": "sao paulo",
        "fim_de_semana_compra": False,
    }


@pytest.fixture
def resposta_valida():
    
    return {
        "prediction_id": 1,
        "prediction": 1,
        "prediction_label": "Atraso previsto",
        "delay_probability": 0.75,
        "message": "Existe risco de atraso na entrega.",
    }


def test_entrada_valida(dados_validos):
    resultado = PredictionInput.model_validate(dados_validos)

    assert isinstance(resultado, PredictionInput)
    assert len(resultado.model_fields_set) == 24


def test_rejeita_campos_obrigatorios_ausentes(dados_validos):
    dados_validos.pop("quantidade_itens")

    with pytest.raises(ValidationError):
        PredictionInput.model_validate(dados_validos)


def test_aceita_valores_none(dados_validos):
    dados_validos["customer_city"] = None

    resultado = PredictionInput.model_validate(dados_validos)

    assert resultado.customer_city is None


def test_rejeita_campos_extras(dados_validos):
    dados_validos["campo_inexistente"] = 10

    with pytest.raises(ValidationError):
        PredictionInput.model_validate(dados_validos)


def test_rejeita_tipo_incorreto(dados_validos):
    dados_validos["quantidade_itens"] = "dois"

    with pytest.raises(ValidationError):
        PredictionInput.model_validate(dados_validos)


def test_rejeita_mes_fora_do_intervalo(dados_validos):
    dados_validos["mes_compra"] = 13

    with pytest.raises(ValidationError):
        PredictionInput.model_validate(dados_validos)


def test_rejeita_sigla_estado_invalida(dados_validos):
    dados_validos["customer_state"] = "sp"

    with pytest.raises(ValidationError):
        PredictionInput.model_validate(dados_validos)


def test_saida_valida(resposta_valida):
    resultado = PredictionOutput.model_validate(resposta_valida)

    assert isinstance(resultado, PredictionOutput)
    assert resultado.prediction == 1
    assert resultado.delay_probability == 0.75


def test_rejeita_classe_invalida(resposta_valida):
    resposta_valida["prediction"] = 2

    with pytest.raises(ValidationError):
        PredictionOutput.model_validate(resposta_valida)


def test_rejeita_probabilidade_fora_do_intervalo(resposta_valida):
    resposta_valida["delay_probability"] = 1.5

    with pytest.raises(ValidationError):
        PredictionOutput.model_validate(resposta_valida)


def test_rejeita_rotulo_invalido(resposta_valida):
    resposta_valida["prediction_label"] = "Risco alto"

    with pytest.raises(ValidationError):
        PredictionOutput.model_validate(resposta_valida)


def test_rejeita_campos_extras_na_saida(resposta_valida):
    resposta_valida["campo_inexistente"] = "teste"

    with pytest.raises(ValidationError):
        PredictionOutput.model_validate(resposta_valida)
