import dask.dataframe as dd
from sklearn.model_selection import train_test_split

def preprocess_large_data(input_path, train_path, test_path):
    # Load the dataset with Dask
    data = dd.read_csv(input_path)  # Handles large CSV files efficiently
    
    # Drop missing values
    data = data.dropna()  # Removes rows with missing values to clean the dataset
    
    # Compute in-memory DataFrame and split into train and test sets
    train, test = train_test_split(data.compute(), test_size=0.2, random_state=42)
    
    # Save processed train and test sets in CSV format
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)

if __name__ == "__main__":
    preprocess_large_data(
        input_path="data/housing.csv",
        train_path="data/train.csv",
        test_path="data/test.csv"
    )
