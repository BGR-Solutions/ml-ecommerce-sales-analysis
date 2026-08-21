import os

from sales_predictor import SalesPredictor


def main():
    # Caminho relativo para o arquivo CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data', 'ecommerce_sales.csv')

    print("--- INICIANDO PROJETO INTEGRADOR: E-COMMERCE ---")
    predictor = SalesPredictor(data_path)
    
    # 1. Análise Descritiva
    print("\n1. ANÁLISE DESCRITIVA:")
    stats = predictor.get_descriptive_analysis()
    print(stats)
    
    # 2. Treinamento
    print("\n2. TREINANDO O MODELO (70% Treino / 30% Teste)...")
    predictor.train_model()
    print("Treinamento concluído com sucesso!")
    
    # 3. Avaliação
    print("\n3. AVALIAÇÃO DO MODELO:")
    metrics = predictor.evaluate_model()
    print(f"Erro Médio Absoluto (MAE): {metrics['MAE']:.2f}")
    print(f"Erro Quadrático Médio (MSE): {metrics['MSE']:.2f}")
    
    print("\n--- PROCESSO FINALIZADO ---")

if __name__ == "__main__":
    main()