import os
import sys
import pandas as pd
import numpy as np
import pickle  # or use joblib if preferred

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from src.exception import CustomException
from src.utils import save_object  # You should implement save_object()

# Create artifacts folder if not exists
os.makedirs("artifacts", exist_ok=True)

def train():
    try:
        df = pd.read_csv("/Users/aryan/-End_To_End_Data_Science_Project/notebook/data/stud.csv") 
        # ✅ 2. Feature Engineering
        X = df.drop(columns=["math_score"])
        y = df["math_score"]

        # ✅ 3. Define preprocessing
        numerical_cols = ["reading_score", "writing_score"]
        categorical_cols = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]

        num_pipeline = Pipeline([
            ('scaler', StandardScaler())
        ])

        cat_pipeline = Pipeline([
            ('onehot', OneHotEncoder(handle_unknown="ignore"))
        ])

        preprocessor = ColumnTransformer([
            ('num', num_pipeline, numerical_cols),
            ('cat', cat_pipeline, categorical_cols)
        ])

        # ✅ 4. Combine into a training pipeline
        model = XGBRegressor()
        pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        # ✅ 5. Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # ✅ 6. Train model
        pipe.fit(X_train, y_train)

        # ✅ 7. Save the preprocessor and model separately (optional split)
        preprocessor.fit(X_train)
        X_train_transformed = preprocessor.transform(X_train)
        model.fit(X_train_transformed, y_train)

        # ✅ 8. Save artifacts
        save_object("artifacts/preprocessor.pkl", preprocessor)
        save_object("artifacts/model.pkl", model)

        print("✅ Training complete. Artifacts saved in /artifacts")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    train()
