import requests
import base64
import json
import sys
import os

# Sobe duas pastas: insert_client/ -> src/ -> import_data_ixc
path_raiz = os.path.abspath(os.path.join(__file__, "../../.."))
sys.path.append(path_raiz)

from config.settings import BASE_URL, API_TOKEN

def inserir_contrato(
    # Parâmetros com valores-padrão
    tipo="I",
    id_cliente="",
    id_vd_contrato="", # Plano do contrato
    id_tipo_contrato="", # Id tipo de de cobrança
    id_modelo="179", # Id modelo do contrato
    id_filial="",
    id_vendedor="1", #Vendedor padrão
    data_base_financeiro="",          
    bloqueio_automatico="N",
    isentar_contrato = "S", 
):
    """
    Função para inserir um contrato via IXC API.
    Cada parâmetro do payload é opcional.
    """

    host = BASE_URL
    url = f"{host}/webservice/v1/cliente_contrato"

    # Gerando o token em Base64
    token = f"{API_TOKEN}".encode("utf-8")
    auth_header = base64.b64encode(token).decode("utf-8")

    # Monta o payload usando os valores dos parâmetros
    payload = {
        "tipo": tipo,
        "id_cliente": id_cliente,
        "id_vd_contrato": id_vd_contrato,
        "id_tipo_contrato": id_tipo_contrato,
        "id_modelo": id_modelo,
        "id_filial": id_filial,
        "id_vendedor": id_vendedor,
        "data_base_financeiro": data_base_financeiro,
        "bloqueio_automatico": bloqueio_automatico,
        "isentar_contrato": isentar_contrato
    }

    headers = {
        "ixcsoft": "",
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
    }

    # Envia requisição
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Mostra a resposta para debug
    print(response.status_code, response.reason)
    print(response.content)
    
    # Retorna o objeto Response
    return response