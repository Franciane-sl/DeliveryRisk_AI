import streamlit as st

from config import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from components.sidebar import render_sidebar

# CONFIGURAÇÕES DA PÁGINA

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded",
)

# ESTILIZAÇÃO GLOBAL

st.markdown(
    """
    <style>

        /* Fundo principal */
        .stApp {
            background-color: #f3f6fb;
        }

        /* Área principal */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1500px;
        }

        /* ==================================================
           BARRA LATERAL
        ================================================== */

        [data-testid="stSidebar"] {
            background-color: #183153;
            border-right: 1px solid #10243d;
        }

        /* Textos da barra lateral */
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stMarkdown {
            color: #ffffff;
        }

        /* Identidade visual */
        .brand-title {
            font-size: 1.55rem;
            font-weight: 750;
            letter-spacing: -0.8px;
            margin-bottom: 0;
            color: #ffffff;
        }

        .brand-subtitle {
            font-size: 0.8rem;
            opacity: 0.75;
            margin-top: 4px;
            color: #dbeafe;
        }

        /* Textos secundários */
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
            color: #cbd5e1;
        }

        /* Divisores da barra lateral */
        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.2);
        }

        /* Navegação */
        [data-testid="stSidebar"] [data-testid="stPageLink"] {
            border-radius: 8px;
        }

        [data-testid="stSidebar"] [data-testid="stPageLink"] a {
            color: #ffffff;
        }

        /* ==================================================
           CONTEÚDO PRINCIPAL
        ================================================== */

        /* Descrição das páginas */
        .section-description {
            color: #64748b;
            font-size: 0.95rem;
        }

        /* Cartões de métricas */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e0e7f0;
            box-shadow: 0 2px 8px rgba(31, 55, 85, 0.04);
        }

        /* Formulários */
        div[data-testid="stForm"] {
            background-color: #ffffff;
            padding: 24px;
            border: 1px solid #e0e7f0;
            border-radius: 14px;
            box-shadow: 0 2px 10px rgba(31, 55, 85, 0.04);
        }

        /* Remove a instrução automática do formulário */
        div[data-testid="InputInstructions"] {
            display: none !important;
        }

        /* Campos numéricos e de texto */
        div[data-testid="stNumberInput"] input,
        div[data-testid="stTextInput"] input {
            border-radius: 8px;
        }

        /* Botões */
        div.stButton > button,
        div.stFormSubmitButton > button {
            background-color: #245b8f;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            transition: background-color 0.2s ease;
        }

        div.stButton > button:hover,
        div.stFormSubmitButton > button:hover {
            background-color: #19466f;
            color: #ffffff;
            border: none;
        }

        /* Expansores */
        div[data-testid="stExpander"] {
            background-color: #ffffff;
            border: 1px solid #e0e7f0;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        /* Divisores do conteúdo principal */
        .stApp hr {
            border-color: #dce4ef;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# BARRA LATERAL

render_sidebar()

# NAVEGAÇÃO


pagina_visao_geral = st.Page(
    "pages/visao_Geral.py",
    title="Visão geral",
    icon=":material/dashboard:",
    default=True,
)

pagina_nova_previsao = st.Page(
    "pages/nova_Previsao.py",
    title="Nova previsão",
    icon=":material/analytics:",
)

pagina_historico = st.Page(
    "pages/historico.py",
    title="Histórico",
    icon=":material/history:",
)


pagina = st.navigation(
    {
        "MENU PRINCIPAL": [
            pagina_visao_geral,
            pagina_nova_previsao,
            pagina_historico,
        ]
    },
    position="sidebar",
)


pagina.run()
