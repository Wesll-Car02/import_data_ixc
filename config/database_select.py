import mariadb
import os
import sys

# Sobe duas pastas: insert_client/ -> src/ -> import_data_ixc
path_raiz = os.path.abspath(os.path.join(__file__, "../"))
sys.path.append(path_raiz)

from settings import BANCO_URL, USER_BANCO, PASS_BANCO

def executa_query(query):
    conn = None
    cursor = None
    resultado = None
    try:
        # Conecta ao banco de dados
        conn = mariadb.connect(
            host=BANCO_URL,        # BANCO_URL deve ser o endereço do host (ex: "localhost")
            user=USER_BANCO,
            password=PASS_BANCO,
            database='ixcprovedor'   # Substitua por seu nome de banco de dados
        )
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Se for uma query SELECT, busca os resultados;
        # Caso contrário, faz o commit e retorna o número de linhas afetadas
        if query.strip().lower().startswith("select"):
            resultado = cursor.fetchall()
        else:
            conn.commit()
            resultado = cursor.rowcount
    except mariadb.Error as e:
        print(f"Erro ao executar a query: {e}")
        resultado = None
    finally:
        # Fecha cursor e conexão, se estiverem abertos
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return resultado

