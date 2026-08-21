# Análise de Vendas e Previsão de Receita (E-commerce) 🛒📈

🇧🇷 Português | 🇺🇸 [Read in English](README.md)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

> **Nota Acadêmica:** Este repositório contém o código e a análise de dados desenvolvidos para o **Projeto Integrador Transdisciplinar em Inteligência Artificial** da faculdade. O objetivo foi aplicar conceitos de regressão linear para resolver um problema real de e-commerce.

## Visão Geral
Uma empresa de e-commerce deseja aprimorar sua estratégia de vendas e precisa entender como a quantidade de itens vendidos afeta diretamente a receita gerada. Este projeto constrói um modelo preditivo para estimar a receita com base nos itens vendidos, identificando tendências para orientar as decisões estratégicas da equipe de negócios.

## Metodologia
- **Algoritmo:** Regressão Linear Simples.
- **Divisão dos Dados:** O conjunto de dados históricos de vendas foi separado em **70% para treinamento** e **30% para teste**.
- **Avaliação do Modelo:** A qualidade das previsões foi medida utilizando as métricas **Erro Médio Absoluto (MAE)** e **Erro Quadrático Médio (MSE)**.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/ml-ecommerce-sales-analysis.git](https://github.com/seu-usuario/ml-ecommerce-sales-analysis.git)
    ```
2. Acesse a pasta do projeto:
    ```bash
    cd ml-ecommerce-sales-analysis
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    ```
4. Ative o ambiente virtual:
    ```bash
    # No Windows:
    .\.venv\Scripts\activate

    # No macOS e Linux:
    source .venv/bin/activate
    ```
5. Instale as dependências necessárias (Pandas, Scikit-learn, Matplotlib):
    ```bash
    pip install .
    ```
6. Execute os Testes Unitários (etapa opcional):
    ```bash
    python -m unittest
    ```
7. Execute o script principal:
    ```bash
    python .\src\main.py
    ```

 ## Licença

Este projeto está sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
