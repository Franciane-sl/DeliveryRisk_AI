import streamlit as st

from api_client import APIClient, APIClientError
from components.charts import (
    render_prediction_distribution,
    render_probability_distribution,
    render_prediction_timeline,
)

from components.metric_cards import render_metric_cards

st.title("Visão geral")

st.markdown(
    """
    <p class="section-description">
        Acompanhe os indicadores e a atividade do DeliveryRisk AI.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()


st.warning(
    "O modelo possui caráter experimental "
    "e apresenta limitações de generalização identificadas "
    "durante sua avaliação."
)

api_client = APIClient()

try:
    with st.spinner("Carregando indicadores..."):
        previsoes = api_client.get_predictions()

except APIClientError as exc:
    st.error(f"Não foi possível carregar os indicadores: {exc.message}")
    st.stop()


if not previsoes:
    st.info("Ainda não existem previsões registradas no sistema.")
    st.stop()


total_previsoes = len(previsoes)

total_atrasos = sum(
    1 for previsao in previsoes
    if previsao["prediction"] == 1
)

total_sem_atraso = total_previsoes - total_atrasos

probabilidade_media = (
    sum(
        previsao["delay_probability"]
        for previsao in previsoes
    ) / total_previsoes
)

st.subheader("Indicadores operacionais")

render_metric_cards([
    {
        "label": "Total de previsões",
        "value": total_previsoes,
    },
    {
        "label": "Atrasos previstos",
        "value": total_atrasos,
    },
    {
        "label": "Sem atraso previsto",
        "value": total_sem_atraso,
    },
    {
        "label": "Probabilidade média de atraso",
        "value": f"{probabilidade_media:.2%}",
        "help": "Média das probabilidades de atraso das previsões realizadas.",
    },
])

st.divider()

st.subheader("Análise das previsões")

render_prediction_distribution(previsoes)

col1, col2 = st.columns(2)

with col1:
    render_probability_distribution(previsoes)

with col2:
    render_prediction_timeline(previsoes)
