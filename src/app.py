
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model/trained_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['features']
    prediction = model.predict([input_data]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
