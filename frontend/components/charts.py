import pandas as pd
import plotly.express as px
import streamlit as st

#Exibindo a distribuição das classificações das previsões
def render_prediction_distribution(previsoes: list) -> None:

    if not previsoes:
        st.info("Não existem previsões para exibir.")
        return

    dados = pd.DataFrame(previsoes)

    distribuicao = (
        dados["prediction_label"]
        .value_counts()
        .rename_axis("Classificação")
        .reset_index(name="Quantidade")
    )

    figura = px.bar(
        distribuicao,
        x="Classificação",
        y="Quantidade",
        title="Distribuição das previsões",
        text="Quantidade",
    )

    figura.update_layout(
        xaxis_title=None,
        yaxis_title="Quantidade de previsões",
        showlegend=False,
    )

    st.plotly_chart(figura, use_container_width=True)

#Exibe a ditribuição das probabilidades de atraso
def render_probability_distribution(previsoes: list) -> None:

    if not previsoes:
        st.info("Não existem probabilidades para exibir.")
        return

    dados = pd.DataFrame(previsoes)

    figura = px.histogram(
        dados,
        x="delay_probability",
        nbins=10,
        title="Distribuição das probabilidades de atraso",
        labels={
            "delay_probability": "Probabilidade de atraso",
            "count": "Quantidade de previsões",
        },
    )

    figura.update_xaxes(tickformat=".0%")

    st.plotly_chart(figura, use_container_width=True)

#Exibe a evolução diária da quantidade de previsões
def render_prediction_timeline(previsoes: list) -> None:

    if not previsoes:
        st.info("Não existem previsões para exibir.")
        return

    dados = pd.DataFrame(previsoes)

    dados["created_at"] = pd.to_datetime(
        dados["created_at"],
        utc=True,
        errors="coerce",
    )

    dados = dados.dropna(subset=["created_at"])

    if dados.empty:
        st.info("Não existem datas válidas para exibir.")
        return

    dados["data"] = dados["created_at"].dt.date

    evolucao = (
        dados.groupby("data")
        .size()
        .reset_index(name="Quantidade")
    )

    figura = px.line(
        evolucao,
        x="data",
        y="Quantidade",
        markers=True,
        title="Evolução das previsões",
        labels={
            "data": "Data",
            "Quantidade": "Quantidade de previsões",
        },
    )

    st.plotly_chart(figura, use_container_width=True)
