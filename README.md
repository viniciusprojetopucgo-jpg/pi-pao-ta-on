# Projeto Integrador IV-A: Sistema de Inteligência de Dados - Pão Tá On 🥖🥤

Este repositório apresenta a infraestrutura de dados desenvolvida para a **Pão Tá On**, com foco em monitoramento comercial e análise de performance de vendas. O projeto utiliza uma arquitetura moderna baseada em containers e processamento em nuvem (Cloud Computing).

## 🏗️ Arquitetura da Solução
A solução foi desenhada para garantir portabilidade e escalabilidade, seguindo o fluxo:
1. **Engine de Processamento**: Script Python utilizando a biblioteca `Faker` para modelagem de cenários e simulação de demanda de mercado.
2. **Containerização**: Empacotamento via **Docker**, garantindo que a aplicação execute de forma idêntica em qualquer ambiente (on-premises ou cloud).
3. **Persistência em Nuvem**: Banco de dados relacional **PostgreSQL** hospedado na plataforma **Railway**.
4. **Business Intelligence (BI)**: Camada de visualização integrada via **Google Looker Studio**.

## 📊 Dashboard de Monitoramento (Tempo Real)
O painel de indicadores permite a análise de faturamento por bairro, performance de produtos e origem de pedidos. O acesso é público e interativo:

👉 [**CLIQUE AQUI PARA ACESSAR O DASHBOARD OFICIAL**](https://lookerstudio.google.com/reporting/a5f30e46-9769-4453-bc86-77f138ef7c05/page/iLOtF)

## 🛠️ Como Executar o Projeto
Para replicar o ambiente de ingestão de dados localmente, utilize os comandos Docker abaixo:

1. **Construir a imagem do sistema:**
   ```powershell
   docker build -t pao_ta_on_app .