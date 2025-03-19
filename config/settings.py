import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "test")  # prod para produção e test para teste

if ENVIRONMENT == "prod":
    API_TOKEN = os.getenv("PROD_API_TOKEN")
    BASE_URL  = os.getenv("PROD_BASE_URL")
else:
    API_TOKEN = os.getenv("TEST_API_TOKEN")
    BASE_URL  = os.getenv("TEST_BASE_URL")

# Para debug
print(f"Ambiente: {ENVIRONMENT}")
print(f"API_TOKEN: {API_TOKEN}")
print(f"BASE_URL: {BASE_URL}")
