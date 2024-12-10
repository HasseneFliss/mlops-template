import os
import dask.dataframe as dd
import joblib
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

def train_large_model(train_path, model_path, scaler_path):
    # Ensure the directory for the model exists
    model_dir = os.path.dirname(model_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Load training data in chunks
    chunksize = 100000  # Process 100,000 rows at a time
    data = dd.read_csv(train_path, blocksize=chunksize)  # Blocksize controls chunk size

    # Initialize the model and scaler
    model = SGDRegressor()
    scaler = StandardScaler()

    # Fit scaler and train model incrementally
    for chunk in data.to_delayed():
        df = chunk.compute()
        X = df.drop(columns=['price'])  # Feature columns
        y = df['price']  # Target column

        # Fit the scaler and transform features
        X_scaled = scaler.partial_fit(X).transform(X)

        # Incrementally train the model
        model.partial_fit(X_scaled, y)

    # Save the trained model and scaler
    joblib.dump(model, model_path)  # Save model for deployment
    joblib.dump(scaler, scaler_path)  # Save scaler for API use

if __name__ == "__main__":
    train_large_model(
        train_path="data/train.csv",
        model_path="model/trained_model.pkl",
        scaler_path="model/scaler.pkl"
    )
