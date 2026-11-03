import os

# Identificação da aplicação
APP_TITLE = "DeliveryRisk AI"
APP_DESCRIPTION = (
    "Sistema de previsão de risco de atraso nas entregas "
    "de pedidos de e-commerce."
)

# Configuração da API
API_BASE_URL = os.getenv(
    "DELIVERYRISK_API_URL",
    "http://127.0.0.1:8000"
)

# Configuração visual
PAGE_ICON = "📦"
LAYOUT = "wide"

# Informações do modelo
MODEL_STATUS = "Experimental"
