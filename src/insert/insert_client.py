import requests
import base64
import json
import sys
import os

# Sobe duas pastas: insert_client/ -> src/ -> import_data_ixc
path_raiz = os.path.abspath(os.path.join(__file__, "../../.."))
sys.path.append(path_raiz)

from config.settings import BASE_URL, API_TOKEN

def inserir_cliente(
    # Parâmetros com valores-padrão
    ativo="S",
    id_tipo_cliente="",
    tipo_cliente_scm="01",
    pais="Brasil",
    tipo_pessoa="",
    razao="",
    ie_identidade="",
    contribuinte_icms="N",
    cnpj_cpf="",
    nacionalidade="Brasileiro",
    data_nascimento="",
    filial_id="",
    filtra_filial="S",
    cep="",
    endereco="",
    numero="",
    complemento="",
    bairro="",
    cidade="",
    referencia="",
    uf="1",
    telefone_celular="",
    email="",
    ultima_atualizacao="CURRENT_TIMESTAMP",
    tipo_assinante="3",
    iss_classificacao_padrao="99",
    tipo_localidade="U",
):
    """
    Função para inserir um cliente via IXC API.
    Cada parâmetro do payload é opcional.
    Se tipo_pessoa vier None, determinamos automaticamente (F ou J) de acordo com o len(cnpj_cpf).
    """

    # **Converter cnpj_cpf para string**
    # cnpj_cpf = str(cnpj_cpf)
    
    # Se não foi passado explicitamente, decidimos aqui
    if not tipo_pessoa:
        if len(cnpj_cpf) == 15:
            tipo_pessoa = "F"
        else:
            tipo_pessoa = "J"
    
    # Tipo de assinante
    if tipo_pessoa == "J": # Por padrão é pessoa F
        tipo_assinante = "1" # Comercial/Industrial

    host = BASE_URL
    url = f"{host}/webservice/v1/cliente"

    # Gerando o token em Base64
    token = f"{API_TOKEN}".encode("utf-8")
    auth_header = base64.b64encode(token).decode("utf-8")

    # Monta o payload usando os valores dos parâmetros
    payload = {
        "ativo": ativo,
        "id_tipo_cliente": id_tipo_cliente,
        "tipo_cliente_scm": tipo_cliente_scm,
        "pais": pais,
        "tipo_pessoa": tipo_pessoa,
        "razao": razao,
        "ie_identidade": ie_identidade,
        "contribuinte_icms": contribuinte_icms,
        "cnpj_cpf": cnpj_cpf,
        "nacionalidade": nacionalidade,
        "data_nascimento": data_nascimento,
        "filial_id": filial_id,
        "filtra_filial": filtra_filial,
        "cep": cep,
        "endereco": endereco,
        "numero": numero,
        "complemento": complemento,
        "bairro": bairro,
        "cidade": cidade,
        "referencia": referencia,
        "uf": uf,
        "telefone_celular": telefone_celular,
        "email": email,
        "ultima_atualizacao": ultima_atualizacao,
        "tipo_assinante": tipo_assinante,
        "iss_classificacao_padrao": iss_classificacao_padrao,
        "tipo_localidade": tipo_localidade,
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