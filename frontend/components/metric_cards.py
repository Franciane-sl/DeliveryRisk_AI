import streamlit as st

# Exibe indicadores em cartões distribuídos em colunas
def render_metric_cards(metrics: list[dict]) -> None:

    if not metrics:
        return

    columns = st.columns(len(metrics))

    for column, metric in zip(columns, metrics):
        column.metric(
            label=metric["label"],
            value=metric["value"],
            delta=metric.get("delta"),
            help=metric.get("help"),
        )
