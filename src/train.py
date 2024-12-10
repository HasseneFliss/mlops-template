import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

def train_model(train_path, model_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Load training data
    data = pd.read_csv(train_path)
    X = data.drop(columns=['Price'])
    y = data['Price']
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model("data/train.csv", "model/trained_model.pkl")
