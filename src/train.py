
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

def train_model(train_path, model_path):
    data = pd.read_csv(train_path)
    X = data.drop(columns=['Price'])
    y = data['Price']
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model("data/train.csv", "model/trained_model.pkl")
