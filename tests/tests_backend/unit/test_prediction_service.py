import pandas as pd
from unittest.mock import MagicMock
from backend.schemas import PredictionInput
from backend.services.prediction_service import predict_delivery_risk

# Cria uma entrada válida para os testes
def create_valid_input():

    return PredictionInput(
        quantidade_itens=2,
        valor_total_produtos=150.0,
        frete_total=25.0,
        quantidade_produtos_distintos=2,
        quantidade_vendedores_distintos=1,
        quantidade_categorias_distintas=2,
        product_weight_g_medio=500.0,
        product_length_cm_medio=20.0,
        product_height_cm_medio=10.0,
        product_width_cm_medio=15.0,
        quantidade_estados_vendedores_distintos=1,
        quantidade_cidades_vendedores_distintas=1,
        ano_compra=2018,
        mes_compra=5,
        dia_mes_compra=15,
        dia_semana_compra=2,
        hora_compra=14,
        customer_zip_code_prefix=12345,
        customer_city="sao paulo",
        customer_state="SP",
        categoria_produto_mais_frequente="beleza",
        seller_state_mais_frequente="SP",
        seller_city_mais_frequente="sao paulo",
        fim_de_semana_compra=False
    )

#Cria um pipeline simulado para os testes
def create_mock_pipeline():
   
    pipeline = MagicMock()

    pipeline.classes_ = [0, 1]
    pipeline.predict.return_value = [1]
    pipeline.predict_proba.return_value = [[0.20, 0.80]]

    return pipeline

#Verifica se a previsão retorna a classe correta
def test_prediction_returns_correct_class():
    
    pipeline = create_mock_pipeline()
    input_data = create_valid_input()

    result = predict_delivery_risk(pipeline, input_data)

    assert result["prediction"] == 1

#Verifica se a probabilidade de atraso é extraída corretamente
def test_prediction_returns_delay_probability():
   
    pipeline = create_mock_pipeline()
    input_data = create_valid_input()

    result = predict_delivery_risk(pipeline, input_data)

    assert result["delay_probability"] == 0.80

#Verifica se os dados são enviados ao pipeline como DataFrame
def test_prediction_uses_dataframe():
    
    pipeline = create_mock_pipeline()
    input_data = create_valid_input()

    predict_delivery_risk(pipeline, input_data)

    received_data = pipeline.predict.call_args[0][0]

    assert isinstance(received_data, pd.DataFrame)
    assert len(received_data) == 1
    assert received_data.shape[1] == 24

#Verifica se a probabilidade da classe 1 é extraída corretamente
def test_prediction_uses_correct_class_index():
   
    pipeline = create_mock_pipeline()

    pipeline.classes_ = [1, 0]
    pipeline.predict_proba.return_value = [[0.75, 0.25]]

    input_data = create_valid_input()

    result = predict_delivery_risk(pipeline, input_data)

    assert result["delay_probability"] == 0.75


# Verifica se o DataFrame contém as features esperadas
def test_prediction_uses_expected_features():

    pipeline = create_mock_pipeline()
    input_data = create_valid_input()

    predict_delivery_risk(pipeline, input_data)

    received_data = pipeline.predict.call_args[0][0]

    expected_columns = list(input_data.model_dump().keys())

    assert list(received_data.columns) == expected_columns
