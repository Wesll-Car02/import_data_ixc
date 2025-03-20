# IXC Data Import

This repository facilitates the import of client, contract, and login data into the IXC database using table migration or data pulling techniques.

## 1.Environment Variables

Before running the code, you need to set the following environment variables:

- **`ENVIRONMENT`**: Specifies the environment to use. Possible values:
  - `test` (default): For testing.
  - `prod`: For production.

- For the `test` environment:
  - **`TEST_API_TOKEN`**: API token for testing.
  - **`TEST_BASE_URL`**: Base URL for the test environment.

- For the `prod` environment:
  - **`PROD_API_TOKEN`**: API token for production.
  - **`PROD_BASE_URL`**: Base URL for the production environment.

### Example

To set the environment variables using the Power Shell:

```powershell
# Configuração do Ambiente

[System.Environment]::SetEnvironmentVariable("ENVIRONMENT", "test", "User")  # ou "prod" para produção

# Para ambiente de teste:
[System.Environment]::SetEnvironmentVariable("TEST_API_TOKEN", "your_token", "User")
[System.Environment]::SetEnvironmentVariable("TEST_BASE_URL", "https://teste.com.br", "User")
# Dados para o banco de teste:
[System.Environment]::SetEnvironmentVariable("TEST_BANCO_URL", "your_url", "User")
[System.Environment]::SetEnvironmentVariable("TEST_USER_BANCO", "your_user_base", "User")
[System.Environment]::SetEnvironmentVariable("TEST_PASS_BANCO", "your_pass_base", "User")

# Para ambiente de produção:
[System.Environment]::SetEnvironmentVariable("PROD_API_TOKEN", "your_token", "User")
[System.Environment]::SetEnvironmentVariable("PROD_BASE_URL", "https://prod.com.br", "User")
# Dados para o banco de produção:
[System.Environment]::SetEnvironmentVariable("PROD_BANCO_URL", "your_url", "User")
[System.Environment]::SetEnvironmentVariable("PROD_USER_BANCO", "your_user_base", "User")
[System.Environment]::SetEnvironmentVariable("PROD_PASS_BANCO", "your_pass_base", "User")
```

Ensure these variables are defined in your environment before running the code.


## 2. Parameters for the `insert_contract.ipynb` Notebook

When using the notebook to insert contracts, please note the fixed parameters as shown in the example below:

```python
# Fixed parameters as per the example call:
contract_type = "I"
model_id = "1"               # Contract model ID (fixed, as per the example)
seller_id = "1"              # Seller ID (fixed, as per the example)
financial_base_date = "01/01/2024"  # Financial base date (can be fixed or calculated according to your rules)
sales_plan_description = "IMPORT"   # Contract type (fixed)
collection_wallet_id = "67"  # Collection wallet ID (fixed)
```

<div style="color: red;">
  <strong>Important Notices:</strong><br><br>
  <strong>Contract Exemption Parameters:</strong><br>
  If the contract is configured for exemption, please note that the contract that migrates as active must have two parameters reversed.<br><br>
  <strong>Pre-Contract:</strong><br>
  The contract configured as a pre-contract must be activated via the bank. Ensure that this rule is correctly applied to avoid inconsistencies.<br><br>
  <strong>Note:</strong> It is essential to review and validate the business rules regarding parameter reversal and bank activation before execution, ensuring the correct insertion and processing of contracts.
</div>
