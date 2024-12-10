import os
import dask.dataframe as dd
import joblib
from sklearn.linear_model import SGDRegressor

def train_large_model(train_path, model_path):
    # Ensure the directory for the model exists
    model_dir = os.path.dirname(model_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Load training data in chunks
    chunksize = 100000  # Process 100,000 rows at a time
    data = dd.read_csv(train_path, blocksize=chunksize)  # Blocksize controls chunk size
    
    # Initialize the model
    model = SGDRegressor()
    
    # Incrementally train the model on each chunk
    for chunk in data.to_delayed():
        df = chunk.compute()  # Compute the chunk into an in-memory DataFrame
        X = df.drop(columns=['price'])  # Feature columns
        y = df['price']  # Target column
        model.partial_fit(X, y)  # Incrementally update the model with the chunk
    
    # Save the trained model
    joblib.dump(model, model_path)  # Save model for deployment

if __name__ == "__main__":
    train_large_model(
        train_path="data/train.csv",
        model_path="model/trained_model.pkl"
    )
