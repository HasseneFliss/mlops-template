import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(test_path, model_path, scaler_path, metrics_path="metrics/metrics.txt"):
    # Load the test dataset
    test_data = pd.read_csv(test_path)
    
    # Check if the 'price' column exists and drop it from X_test
    if 'price' not in test_data.columns:
        raise KeyError("'price' column not found in the dataset")
    
    X_test = test_data.drop(columns=['price'])
    y_test = test_data['price']

    # Load the trained model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Scale the test features
    X_test_scaled = scaler.transform(X_test)

    # Make predictions
    predictions = model.predict(X_test_scaled)

    # Calculate accuracy metrics
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Save metrics to a file
    with open(metrics_path, "w") as f:
        f.write(f"Mean Squared Error (MSE): {mse}\n")
        f.write(f"Mean Absolute Error (MAE): {mae}\n")
        f.write(f"R² Score: {r2}\n")

if __name__ == "__main__":
    evaluate_model(
        test_path="data/test.csv",
        model_path="model/trained_model.pkl",
        scaler_path="model/scaler.pkl"
    )
