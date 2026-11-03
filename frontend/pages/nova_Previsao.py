import streamlit as st

from api_client import APIClient, APIClientError
from components.prediction_result import render_prediction_result
from utils.validators import validate_prediction_data


st.title("Nova previsão")

st.markdown(
    """
    <p class="section-description">
        Informe as características de um pedido para estimar
        o risco de atraso na entrega.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()


with st.form(
    "prediction_form",
    clear_on_submit=False,
    enter_to_submit=False,
):

    with st.expander("1. Informações gerais do pedido", expanded=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            quantidade_itens = st.number_input(
                "Quantidade de itens",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

        with col2:
            quantidade_produtos_distintos = st.number_input(
                "Produtos distintos",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

        with col3:
            quantidade_vendedores_distintos = st.number_input(
                "Vendedores distintos",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

        col1, col2, col3 = st.columns(3)

        with col1:
            quantidade_categorias_distintas = st.number_input(
                "Categorias distintas",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

        with col2:
            quantidade_estados_vendedores_distintos = st.number_input(
                "Estados de vendedores distintos",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

        with col3:
            quantidade_cidades_vendedores_distintas = st.number_input(
                "Cidades de vendedores distintas",
                min_value=1,
                value=None,
                step=1,
                placeholder="Informe a quantidade",
            )

    with st.expander("2. Valores e dimensões dos produtos"):
        col1, col2 = st.columns(2)

        with col1:
            valor_total_produtos = st.number_input(
                "Valor total dos produtos",
                min_value=0.0,
                value=None,
                step=0.01,
                placeholder="Ex.: 150.00",
            )

        with col2:
            frete_total = st.number_input(
                "Frete total",
                min_value=0.0,
                value=None,
                step=0.01,
                placeholder="Ex.: 25.50",
            )

        col1, col2 = st.columns(2)

        with col1:
            product_weight_g_medio = st.number_input(
                "Peso médio (gramas)",
                min_value=0.0,
                value=None,
                step=0.01,
            )

            product_length_cm_medio = st.number_input(
                "Comprimento médio (cm)",
                min_value=0.0,
                value=None,
                step=0.01,
            )

        with col2:
            product_height_cm_medio = st.number_input(
                "Altura média (cm)",
                min_value=0.0,
                value=None,
                step=0.01,
            )

            product_width_cm_medio = st.number_input(
                "Largura média (cm)",
                min_value=0.0,
                value=None,
                step=0.01,
            )

    with st.expander("3. Data e horário da compra"):
        col1, col2, col3 = st.columns(3)

        with col1:
            ano_compra = st.number_input(
                "Ano da compra",
                value=None,
                step=1,
            )

        with col2:
            mes_compra = st.number_input(
                "Mês da compra",
                min_value=1,
                max_value=12,
                value=None,
                step=1,
            )

        with col3:
            dia_mes_compra = st.number_input(
                "Dia do mês",
                min_value=1,
                max_value=31,
                value=None,
                step=1,
            )

        col1, col2 = st.columns(2)

        with col1:
            dia_semana_compra = st.number_input(
                "Dia da semana (0 = segunda, 6 = domingo)",
                min_value=0,
                max_value=6,
                value=None,
                step=1,
            )

        with col2:
            hora_compra = st.number_input(
                "Hora da compra",
                min_value=0,
                max_value=23,
                value=None,
                step=1,
            )

        fim_de_semana_compra = st.checkbox(
            "A compra foi realizada no fim de semana?"
        )

    with st.expander("4. Localização do cliente"):
        col1, col2 = st.columns(2)

        with col1:
            customer_zip_code_prefix = st.number_input(
                "Prefixo do CEP do cliente",
                min_value=0,
                max_value=99999,
                value=None,
                step=1,
            )

            customer_city = st.text_input(
                "Cidade do cliente",
                max_chars=100,
            )

        with col2:
            customer_state = st.text_input(
                "Estado do cliente (UF)",
                max_chars=2,
                placeholder="Ex.: SC",
            )

    with st.expander("5. Características dos vendedores e produtos"):
        col1, col2 = st.columns(2)

        with col1:
            categoria_produto_mais_frequente = st.text_input(
                "Categoria de produto mais frequente",
                max_chars=100,
            )

            seller_state_mais_frequente = st.text_input(
                "Estado mais frequente dos vendedores (UF)",
                max_chars=2,
                placeholder="Ex.: SP",
            )

        with col2:
            seller_city_mais_frequente = st.text_input(
                "Cidade mais frequente dos vendedores",
                max_chars=100,
            )

    st.divider()

    submitted = st.form_submit_button(
        "Gerar previsão",
        type="primary",
        use_container_width=True,
    )


if submitted:

    dados = {
        "quantidade_itens": quantidade_itens,
        "quantidade_produtos_distintos": quantidade_produtos_distintos,
        "quantidade_vendedores_distintos": quantidade_vendedores_distintos,
        "quantidade_categorias_distintas": quantidade_categorias_distintas,
        "quantidade_estados_vendedores_distintos": quantidade_estados_vendedores_distintos,
        "quantidade_cidades_vendedores_distintas": quantidade_cidades_vendedores_distintas,
        "valor_total_produtos": valor_total_produtos,
        "frete_total": frete_total,
        "product_weight_g_medio": product_weight_g_medio,
        "product_length_cm_medio": product_length_cm_medio,
        "product_height_cm_medio": product_height_cm_medio,
        "product_width_cm_medio": product_width_cm_medio,
        "ano_compra": ano_compra,
        "mes_compra": mes_compra,
        "dia_mes_compra": dia_mes_compra,
        "dia_semana_compra": dia_semana_compra,
        "hora_compra": hora_compra,
        "customer_zip_code_prefix": customer_zip_code_prefix,
        "customer_city": customer_city.strip(),
        "customer_state": customer_state.strip().upper(),
        "categoria_produto_mais_frequente": categoria_produto_mais_frequente.strip(),
        "seller_state_mais_frequente": seller_state_mais_frequente.strip().upper(),
        "seller_city_mais_frequente": seller_city_mais_frequente.strip(),
        "fim_de_semana_compra": fim_de_semana_compra,
    }

    erros = validate_prediction_data(dados)

    if erros:
        for erro in erros:
            st.error(erro)

    else:
        try:
            api_client = APIClient()

            with st.spinner("Analisando os dados do pedido..."):
                resultado = api_client.predict(dados)

            st.session_state["prediction_result"] = resultado

        except APIClientError as exc:
            st.error(f"Erro ao realizar previsão: {exc.message}")


resultado = st.session_state.get("prediction_result")

if resultado:
    render_prediction_result(resultado)
