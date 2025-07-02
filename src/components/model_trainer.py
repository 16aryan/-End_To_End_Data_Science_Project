import os, sys
from dataclasses import dataclass
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoost": CatBoostRegressor(verbose=False),
                "AdaBoost": AdaBoostRegressor()
            }

            params = {
                "Decision Tree": {"criterion": ['squared_error', 'friedman_mse']},
                "Random Forest": {"n_estimators": [8, 64, 128]},
                "Gradient Boosting": {
                    "learning_rate": [0.1, 0.01],
                    "n_estimators": [32, 128]
                },
                "XGBRegressor": {"learning_rate": [0.1, 0.01], "n_estimators": [32, 128]},
                "CatBoost": {"depth": [6, 8], "learning_rate": [0.01, 0.1], "iterations": [50, 100]},
                "AdaBoost": {"learning_rate": [0.1, 0.01], "n_estimators": [32, 128]},
                "Linear Regression": {}
            }

            scores = evaluate_models(X_train, y_train, X_test, y_test, models, params)
            best_model_name = max(scores, key=scores.get)
            best_score = scores[best_model_name]
            if best_score < 0.6:
                raise CustomException("No acceptable model found", sys)

            best_model = models[best_model_name]
            save_object(self.config.trained_model_file_path, best_model)
            logging.info(f"Best Model: {best_model_name} | Score: {best_score}")

            return r2_score(y_test, best_model.predict(X_test))
        except Exception as e:
            raise CustomException(e, sys)