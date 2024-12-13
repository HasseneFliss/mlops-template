import os
import dask.dataframe as dd
import joblib
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_squared_error

def train_large_model(train_path, model_path, scaler_path):
    # Set up MLflow
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "https://mlflow.dev-avaxialabs.com")) # to add credentials of mlflow to login here
    mlflow.set_experiment("Large Model Training")
    
    with mlflow.start_run():
        # Ensure directories exist
        model_dir = os.path.dirname(model_path)
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        # Initialize model and scaler
        model = SGDRegressor()
        scaler = StandardScaler()

        # Metrics to track
        mse_list = []

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

            # Evaluate on the current chunk (optional)
            predictions = model.predict(X_scaled)
            mse = mean_squared_error(y, predictions)
            mse_list.append(mse)

        # Save model and scaler
        joblib.dump(model, model_path)
        joblib.dump(scaler, scaler_path)

        # Log model, scaler, and metrics to MLflow
        mlflow.log_param("model_type", "SGDRegressor")
        mlflow.log_param("chunksize", chunksize)
        mlflow.log_metric("average_mse", sum(mse_list) / len(mse_list))
        mlflow.sklearn.log_model(model, artifact_path="trained_model")
        
        print(f"Model logged with average MSE: {sum(mse_list) / len(mse_list]}")

if __name__ == "__main__":
    train_large_model(
        train_path="data/train.csv",
        model_path="model/trained_model.pkl",
        scaler_path="model/scaler.pkl"
    )
