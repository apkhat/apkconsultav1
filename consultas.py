import time
from tqdm import tqdm

# Função para simular o carregamento
def carregar_tela():
    print("Carregando a outra tela...")
    for _ in tqdm(range(10), desc="Carregando", ncols=100):
        time.sleep(0.5)  # Simula um processo de carregamento
    print("Carregamento concluído. Bem-vindo à Consultas!")

# Chamando a função de carregamento
carregar_tela()
