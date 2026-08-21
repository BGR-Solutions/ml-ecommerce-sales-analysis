import os
import unittest

import numpy as np
import pandas as pd

from src.sales_predictor import SalesPredictor


class TestSalesPredictor(unittest.TestCase):
    def setUp(self):
        """Prepara um CSV temporário para os testes."""
        self.test_csv = "test_data.csv"
        # Dados fictícios perfeitamente lineares (y = 10x) para teste
        data = {
            "codigo_item": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "quantidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "receita": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        }
        pd.DataFrame(data).to_csv(self.test_csv, index=False)
        self.predictor = SalesPredictor(self.test_csv)

    def tearDown(self):
        """Limpa o arquivo temporário após os testes."""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_load_data(self):
        data = self.predictor.load_data()
        self.assertEqual(len(data), 10)
        self.assertIn("receita", data.columns)

    def test_train_and_split(self):
        self.predictor.train_model()
        # 30% de 10 amostras = 3 amostras para teste
        self.assertEqual(len(self.predictor.X_test), 3)
        self.assertEqual(len(self.predictor.X_train), 7)
        self.assertIsNotNone(self.predictor.model.coef_)

    def test_evaluate_model(self):
        self.predictor.train_model()
        metrics = self.predictor.evaluate_model()
        # Como os dados de teste são perfeitamente lineares, o erro deve ser quase 0
        self.assertIn("MAE", metrics)
        self.assertIn("MSE", metrics)
        self.assertAlmostEqual(metrics["MAE"], 0.0, places=5)
        self.assertAlmostEqual(metrics["MSE"], 0.0, places=5)

if __name__ == "__main__":
    unittest.main()