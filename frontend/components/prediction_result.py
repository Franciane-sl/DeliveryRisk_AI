
import streamlit as st

# Exibe o resultado de uma previsão realizada pela API
def render_prediction_result(resultado: dict) -> None:

    if not resultado:
        return

    st.divider()
    st.subheader("Resultado da previsão")

    prediction = resultado["prediction"]
    prediction_label = resultado["prediction_label"]
    delay_probability = resultado["delay_probability"]

    if prediction == 1:
        st.error(prediction_label)
    else:
        st.success(prediction_label)

    col1, col2 = st.columns(2)

    col1.metric(
        "Probabilidade de atraso",
        f"{delay_probability:.2%}",
    )

    col2.metric(
        "ID da previsão",
        resultado["prediction_id"],
    )

    st.info(resultado["message"])
