import streamlit as st

from api_client import APIClient, APIClientError
from components.metric_cards import render_metric_cards


st.title("Histórico de previsões")

st.markdown(
    """
    <p class="section-description">
        Consulte e gerencie as previsões realizadas pelo sistema.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

if "mensagem_sucesso" in st.session_state:
    st.success(st.session_state.pop("mensagem_sucesso"))

api_client = APIClient()

try:
    with st.spinner("Carregando histórico..."):
        previsoes = api_client.get_predictions()

except APIClientError as exc:
    st.error(f"Não foi possível carregar o histórico: {exc.message}")
    st.stop()


if not previsoes:
    st.info("Nenhuma previsão foi registrada até o momento.")
    st.stop()


total_previsoes = len(previsoes)

total_atrasos = sum(
    1 for previsao in previsoes
    if previsao["prediction"] == 1
)

total_sem_atraso = total_previsoes - total_atrasos

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
])

st.divider()

st.subheader("Previsões registradas")

dados_historico = []

for previsao in previsoes:
    dados_historico.append({
        "ID": previsao["id"],
        "Classificação": previsao["prediction_label"],
        "Probabilidade de atraso": (
            f"{previsao['delay_probability']:.2%}"
        ),
        "Data da previsão": previsao["created_at"],
    })

st.dataframe(
    dados_historico,
    use_container_width=True,
    hide_index=True,
)

st.divider()

st.subheader("Detalhes da previsão")

ids_previsoes = [
    previsao["id"]
    for previsao in previsoes
]

id_selecionado = st.selectbox(
    "Selecione uma previsão",
    options=ids_previsoes,
    format_func=lambda valor: f"Previsão #{valor}",
)

try:
    detalhe = api_client.get_prediction(id_selecionado)

    col1, col2 = st.columns(2)

    col1.metric(
        "Classificação",
        detalhe["prediction_label"],
    )

    col2.metric(
        "Probabilidade de atraso",
        f"{detalhe['delay_probability']:.2%}",
    )

    st.caption(f"Data da previsão: {detalhe['created_at']}")

    with st.expander("Visualizar dados utilizados na previsão"):
        if detalhe.get("input_data"):
            st.json(detalhe["input_data"])
        else:
            st.info("Dados de entrada não disponíveis.")

except APIClientError as exc:
    st.error(f"Não foi possível consultar os detalhes: {exc.message}")
    st.stop()


st.divider()

st.subheader("Gerenciar previsão")

confirmar_exclusao = st.checkbox(
    f"Confirmo que desejo excluir a previsão #{id_selecionado}"
)

if st.button(
    "Excluir previsão",
    type="secondary",
    disabled=not confirmar_exclusao,
):
    try:
        api_client.delete_prediction(id_selecionado)

        st.session_state["mensagem_sucesso"] = (
            f"Previsão #{id_selecionado} excluída com sucesso."
        )

        st.rerun()

    except APIClientError as exc:
        st.error(
            f"Não foi possível excluir a previsão: {exc.message}"
        )