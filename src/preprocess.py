
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    data = data.dropna()  # Example preprocessing
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    train.to_csv(f"{output_path}/train.csv", index=False)
    test.to_csv(f"{output_path}/test.csv", index=False)

if __name__ == "__main__":
    preprocess_data("data/housing.csv", "data")
