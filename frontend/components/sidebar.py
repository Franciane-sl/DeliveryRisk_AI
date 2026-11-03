import streamlit as st

from config import APP_TITLE
from api_client import APIClient, APIClientError

# Renderiza a identidade visual e o status da API na barra lateral
def render_sidebar() -> None:
   
    with st.sidebar:

        st.markdown(
            f"""
            <div>
                <p class="brand-title">📦 {APP_TITLE}</p>
                <p class="brand-subtitle">
                    Inteligência preditiva para entregas
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.caption("PLATAFORMA DE ANÁLISE PREDITIVA")

        st.divider()

        st.caption("STATUS DA API")

        api_client = APIClient()

        try:
            health = api_client.get_health()

            if health.get("status") == "healthy" and health.get("model_loaded"):
                st.success("API conectada")

            elif health.get("status") == "healthy":
                st.warning("API conectada, modelo não carregado")

            else:
                st.warning("API disponível, mas não saudável")

        except APIClientError:
            st.error("API indisponível")
