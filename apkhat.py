import os
import sys
import time
from tqdm import tqdm
import requests

# Função para carregar a tela
def carregar_tela():
    print("Iniciando script, aguarde...")
    for i in tqdm(range(10)):
        time.sleep(1)
    os.system('clear')

# Função para instalar dependências
def instalar_dependencias():
    print("As dependências serão baixadas em breve")
    for i in tqdm(range(2)):
        time.sleep(1)

    os.system('pip install -r requirements.txt')  # Corrigido para instalar a partir do arquivo requirements.txt
    os.system('clear')

# Função para executar a API
def executar_api():
    print("SISTEMA INICIADO COM SUCESSO")
    print("Script 12% - Alguns CEPs podem não funcionar")

    cep = input("Digite o CEP para consulta: ")
    print("RESULTADOS ABAIXO")

    url = f'https://cdn.apicep.com/file/apicep/{cep}.json'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f'Código CEP: {data["code"]}')
        print(f'Estado: {data["state"]}')
        print(f'Cidade: {data["city"]}')
    else:
        print("Não foi possível completar esta ação")

# Função para reiniciar o script da tela 1
def reiniciar_script():
    os.system("clear")
    print("Reiniciando o script da tela 1...")
    time.sleep(2)
    os.system("python apkhat.py")  # Substitua 'tela1.py' pelo nome do seu arquivo da tela 1
    sys.exit()

# Tela principal
while True:
    carregar_tela()
    instalar_dependencias()
    executar_api()

    x = input('01 - Reiniciar consulta\n02 - consulta especial\n: ')

    if x == '1':
        reiniciar_script()
    elif x == '2':
        os.system("clear")
        os.system("python consultas.py")
        exit()
