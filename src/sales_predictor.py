import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


class SalesPredictor:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = None
        self.model = LinearRegression()
        self.X_train, self.X_test, self.y_train, self.y_test = [None] * 4

    def load_data(self):
        """Carrega os dados do CSV."""
        self.data = pd.read_csv(self.data_path)
        return self.data

    def get_descriptive_analysis(self):
        """Retorna a análise descritiva básica (média, desvio padrão, etc)."""
        if self.data is None:
            self.load_data()
        return self.data.describe()

    def train_model(self):
        """Prepara os dados (70/30) e treina o modelo de regressão linear."""
        if self.data is None:
            self.load_data()
        
        # Variável independente (X) e dependente (y)
        X = self.data[['quantidade']]
        y = self.data['receita']

        # Separação 70% treino e 30% teste
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        
        # Treinamento do modelo
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """Avalia o modelo utilizando MAE e MSE."""
        if self.X_test is None:
            raise ValueError("O modelo precisa ser treinado antes da avaliação.")
        
        predictions = self.model.predict(self.X_test)
        
        mae = mean_absolute_error(self.y_test, predictions)
        mse = mean_squared_error(self.y_test, predictions)
        
        return {"MAE": mae, "MSE": mse}