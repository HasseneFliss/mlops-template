# House Price Prediction Model

This project is a machine learning pipeline that predicts house prices based on specific input features such as size, number of bedrooms, and number of bathrooms. The application uses a Flask API to serve the predictions.

## **How It Works**

### **1. Data Preprocessing**
- The dataset (e.g., `housing.csv`) contains historical data, including:
  - Size of the house (e.g., square footage)
  - Number of bedrooms
  - Number of bathrooms
  - House price (target variable)
- Preprocessing steps:
  - Remove missing values.
  - Split the dataset into training and testing sets.

### **2. Model Training**
- **Algorithm**: Linear Regression
  - The model learns the relationship between the input features (e.g., size, rooms) and the target variable (house price).
- **Output**: A trained model (`trained_model.pkl`) saved for deployment.

### **3. Model Prediction**
- The trained model takes new input data, such as:
  ```json
  {
    "features": [1200, 3, 2]
  }
