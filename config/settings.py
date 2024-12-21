import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

# Identifica o ambiente atual (padrão: "test")
ENVIRONMENT = os.getenv("ENVIRONMENT", "test")

# Se for "test", pega as variáveis de teste; se for "prod", pega as variáveis de produção
if ENVIRONMENT == "prod":
    API_TOKEN = os.getenv("PROD_API_TOKEN")
    BASE_URL = os.getenv("PROD_BASE_URL")
else:
    # Caso contrário, assume que é ambiente de teste (ou outro)
    API_TOKEN = os.getenv("TEST_API_TOKEN")
    BASE_URL = os.getenv("TEST_BASE_URL")

# Para debug
print(f"Usando ambiente: {ENVIRONMENT}")
# print(f"API_TOKEN: {API_TOKEN}")
# print(f"BASE_URL: {BASE_URL}")
