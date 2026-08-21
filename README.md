# E-commerce Sales Analysis & Revenue Prediction 🛒📈

🇺🇸 English | 🇧🇷 [Leia em Português](README.pt-br.md)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

> **Academic Note:** This repository contains the code and data analysis developed for the "Projeto Integrador Transdisciplinar em Inteligência Artificial" (Transdisciplinary Integrative Project in Artificial Intelligence) for my university degree. The objective is to apply Linear Regression concepts to solve a real-world e-commerce problem.

## Overview
An e-commerce company wants to improve its sales strategy and needs to understand how the quantity of items sold directly affects the generated revenue. This project builds a predictive machine learning model to estimate revenue based on the number of items sold, identifying patterns to help the sales team optimize operations.

## Methodology
- **Algorithm:** Simple Linear Regression.
- **Data Split:** The historical sales dataset was divided into **70% for training** and **30% for testing**.
- **Model Evaluation:** The performance of the algorithm is measured using **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)**.

## How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/ml-ecommerce-sales-analysis.git](https://github.com/your-username/ml-ecommerce-sales-analysis.git)
   ```
2. Navigate to the project directory:
    ```bash
    cd ml-ecommerce-sales-analysis
    ```
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    # On Windows:
    venv\Scripts\activate

    # On macOS and Linux:
    source venv/bin/activate
    ```
5. Install the required libraries (Pandas, Scikit-learn, Matplotlib):
    ```bash
    pip install .
    ```
6. Run the Unity Tests (optional step):
    ```bash
    python -m unittest
    ```
7. Run the Python script:
    ```bash
    python src/main.py
    ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
