import pandas as pd
import random
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from faker import Faker

# Configuração do Faker para nomes brasileiros
fake = Faker('pt_BR')

# 1. Configuração do Banco de Dados (Railway)
DB_URL = "postgresql://postgres:reTXBSCGRUssHybkJKUPKtHwAZGjbewO@gondola.proxy.rlwy.net:31447/railway"
engine = create_engine(DB_URL)

# 2. Dados reais fornecidos pelo "Pão Tá On" (Angra dos Reis)
bairros = [
    'Parque Mambucaba', 
    'Vila Residencial', 
    'Vila Histórica', 
    'Praia Brava'
]

produtos_cardapio = {
    'Pão de alho de contra filé': 35.00,
    'Pão de alho misto': 28.00,
    'Batata Maluca': 45.00,
    'Explosão de Frango': 32.00
}

origens_pedido = ['iFood', 'Site Próprio']

# 3. Gerando vendas simuladas com múltiplos itens por pedido
print("Iniciando geração de dados simulados (Lógica de Múltiplos Itens)...")
data_vendas = []
total_sessoes_compra = 80 # Simula 80 pedidos completos

for _ in range(total_sessoes_compra):
    # Cada sessão representa um PEDIDO único de um cliente
    cliente_sessao = fake.name()
    bairro_sessao = random.choice(bairros)
    origem_sessao = random.choice(origens_pedido)
    data_venda_sessao = datetime.now() - timedelta(days=random.randint(0, 30))
    
    # Define de 1 a 4 itens diferentes para este mesmo pedido
    quantidade_itens_pedido = random.randint(1, 4)
    produtos_ja_escolhidos = []

    for _ in range(quantidade_itens_pedido):
        # Garante que o cliente não peça o mesmo produto duplicado no mesmo pedido
        nome_prod = random.choice(list(produtos_cardapio.keys()))
        while nome_prod in produtos_ja_escolhidos:
             nome_prod = random.choice(list(produtos_cardapio.keys()))
        
        produtos_ja_escolhidos.append(nome_prod)

        venda = {
            'cliente': cliente_sessao,
            'bairro': bairro_sessao,
            'produto': nome_prod,
            'valor': produtos_cardapio[nome_prod],
            'origem': origem_sessao,
            'data_venda': data_venda_sessao
        }
        data_vendas.append(venda)

# 4. Processamento e Carga (ETL) para a Nuvem
try:
    df = pd.DataFrame(data_vendas)
    
    # Envia os dados para a tabela 'vendas_pao_ta_on'
    df.to_sql('vendas_pao_ta_on', engine, if_exists='append', index=False)
    
    print("-" * 40)
    print("SUCESSO!")
    print(f"Foram processados {len(df)} itens vendidos em {total_sessoes_compra} pedidos.")
    print("Os dados agora refletem comportamentos de compra realistas.")
    print("-" * 40)

except Exception as e:
    print(f"ERRO ao conectar ou enviar dados: {e}")