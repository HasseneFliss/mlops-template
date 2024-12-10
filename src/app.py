from flask import Flask, request, jsonify
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("model/trained_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the JSON request
    input_data = request.json['features']
    
    # Scale the input features
    input_scaled = scaler.transform([input_data])  # Scale input features
    
    # Predict using the model
    prediction = model.predict(input_scaled).tolist()
    
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
