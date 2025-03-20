# IXC Data Import

This repository facilitates the import of client, contract, and login data into the IXC database using table migration or data pulling techniques.

## Environment Variables

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
# Set environment

[System.Environment]::SetEnvironmentVariable("ENVIRONMENT", "test", "User") # or prod

# For testing
[System.Environment]::SetEnvironmentVariable("TEST_API_TOKEN", "your_token", "User")
[System.Environment]::SetEnvironmentVariable("TEST_BASE_URL", "https://teste.com.br", "User")

[System.Environment]::SetEnvironmentVariable("TEST_BANCO_URL", "your_url", "User")
[System.Environment]::SetEnvironmentVariable("TEST_USER_BANCO", "your_user_base", "User")
[System.Environment]::SetEnvironmentVariable("TEST_PASS_BANCO", "your_pass_base", "User")

# For production
[System.Environment]::SetEnvironmentVariable("PROD_API_TOKEN", "your_token", "User")
[System.Environment]::SetEnvironmentVariable("PROD_BASE_URL", "https://prod.com.br", "User")
```

Ensure these variables are defined in your environment before running the code.