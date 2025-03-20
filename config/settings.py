import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "test")  # prod para produção e test para teste

if ENVIRONMENT == "prod":
    API_TOKEN = os.getenv("PROD_API_TOKEN")
    BASE_URL  = os.getenv("PROD_BASE_URL")
else:
    API_TOKEN = os.getenv("TEST_API_TOKEN")
    BASE_URL  = os.getenv("TEST_BASE_URL")
    BANCO_URL = os.getenv("TEST_BANCO_URL")
    USER_BANCO = os.getenv("TEST_USER_BANCO")
    PASS_BANCO = os.getenv("TEST_PASS_BANCO")

# Para debug
print(f"Ambiente: {ENVIRONMENT}")
print(f"API_TOKEN: {API_TOKEN}")
print(f"BASE_URL: {BASE_URL}")
print(f"BANCO_URL: {BANCO_URL}")
print(f"USER_BANCO: {USER_BANCO}")
print(f"PASS_BANCO: {PASS_BANCO}")
