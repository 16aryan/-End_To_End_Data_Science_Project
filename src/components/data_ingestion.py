import os, sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class DataIngestion:
    def __init__(self, raw_path="notebook/data/stud.csv", out_dir="artifacts"):
        self.raw_path = raw_path
        self.train_path = os.path.join(out_dir, "train.csv")
        self.test_path = os.path.join(out_dir, "test.csv")
        self.raw_out = os.path.join(out_dir, "data.csv")
        os.makedirs(out_dir, exist_ok=True)

    def run(self):
        try:
            logging.info("Ingesting data...")
            df = pd.read_csv(self.raw_path)
            df.to_csv(self.raw_out, index=False)
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            train.to_csv(self.train_path, index=False)
            test.to_csv(self.test_path, index=False)
            logging.info("Ingestion complete.")
            return self.train_path, self.test_path
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        train, test = DataIngestion().run()
        train_arr, test_arr, _ = DataTransformation().initiate_data_transformation(train, test)
        score = ModelTrainer().initiate_model_trainer(train_arr, test_arr)
        print(f"✅ R² Score: {score:.4f}")
    except Exception as e:
        print(f"❌ Error: {e}")