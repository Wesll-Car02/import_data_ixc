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

To set the environment variables using the command line (CMD):

```cmd
# Set environment
set ENVIRONMENT=test   # or prod

# For testing
set TEST_API_TOKEN=your_test_api_token
set TEST_BASE_URL=https://test-api.example.com

# For production
set PROD_API_TOKEN=your_prod_api_token
set PROD_BASE_URL=https://prod-api.example.com
```

Ensure these variables are defined in your environment before running the code.