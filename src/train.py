import os
import dask.dataframe as dd
import joblib
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

def train_large_model(train_path, model_path, scaler_path):
    # Ensure directories exist
    model_dir = os.path.dirname(model_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Initialize model and scaler
    model = SGDRegressor()
    scaler = StandardScaler()

    # Load training data
    chunksize = 100000  # Process data in chunks
    data = dd.read_csv(train_path, blocksize=chunksize)
    for chunk in data.to_delayed():
        df = chunk.compute()
        X = df.drop(columns=['price'])
        y = df['price']

        # Fit and transform features
        X_scaled = scaler.partial_fit(X).transform(X)
        model.partial_fit(X_scaled, y)

    # Save model and scaler
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

if __name__ == "__main__":
    train_large_model(
        train_path="data/train.csv",
        model_path="model/trained_model.pkl",
        scaler_path="model/scaler.pkl"
    )
