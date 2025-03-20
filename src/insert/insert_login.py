import requests
import base64
import json
import sys
import os

# Sobe duas pastas: insert_client/ -> src/ -> import_data_ixc
path_raiz = os.path.abspath(os.path.join(__file__, "../../.."))
sys.path.append(path_raiz)

from config.settings import BASE_URL, API_TOKEN

def inserir_radusuarios(
    autenticacao="L",
    tipo_conexao_mapa="F",
    id_cliente="",
    id_contrato="",
    id_grupo="",
    login="",
    senha_md5="N",
    senha="",
    login_simultaneo="1",
    ativo="S",
    auto_preencher_ip="S",
    fixar_ip="N",
    relacionar_ip_ao_login="N",
    autenticacao_por_mac="N",
    auto_preencher_mac="S",
    relacionar_mac_ao_login="S",
    tipo_vinculo_plano="D",
    cep="",
    endereco="",
    numero="",
    complemento="",
    bairro="",
    cidade="",
):
    """
    Função para inserir um usuário via IXC API na rota /webservice/v1/radusuarios.
    Todos os campos são obrigatórios conforme a documentação.
    """
    host = BASE_URL
    url = f"{host}/webservice/v1/radusuarios"

    # Gerando o token em Base64
    token = f"{API_TOKEN}".encode("utf-8")
    auth_header = base64.b64encode(token).decode("utf-8")

    # Monta o payload com os parâmetros fornecidos
    payload = {
        "autenticacao": autenticacao,
        "tipo_conexao_mapa": tipo_conexao_mapa,
        "id_cliente": id_cliente,
        "id_contrato": id_contrato,
        "id_grupo": id_grupo,
        "login": login,
        "senha_md5": senha_md5,
        "senha": senha,
        "login_simultaneo": login_simultaneo,
        "ativo": ativo,
        "auto_preencher_ip": auto_preencher_ip,
        "fixar_ip": fixar_ip,
        "relacionar_ip_ao_login": relacionar_ip_ao_login,
        "autenticacao_por_mac": autenticacao_por_mac,
        "auto_preencher_mac": auto_preencher_mac,
        "relacionar_mac_ao_login": relacionar_mac_ao_login,
        "tipo_vinculo_plano": tipo_vinculo_plano,
        "cep":cep,
        "endereco":endereco,
        "numero": numero,
        "complemento": complemento,
        "bairro": bairro,
        "cidade": cidade,
    }

    headers = {
        "ixcsoft": "",
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json"
    }

    # Envia a requisição POST
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Mostra a resposta para debug
    print(response.status_code, response.reason)
    print(response.content)
    
    # Retorna o objeto Response
    return response
