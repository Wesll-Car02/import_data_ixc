import pandas as pd

def carregar_tabela_excel(caminho_excel: str) -> pd.DataFrame:
    """Carrega o arquivo Excel em um DataFrame Pandas."""
    try:
        df = pd.read_excel(caminho_excel)
        return df
    except Exception as e:
        print(f"Erro ao carregar Excel: {e}")
        return pd.DataFrame()
