FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application source code
COPY src/ ./src/

# Copy the trained model artifact from the downloaded location
COPY model/trained_model.pkl ./model/trained_model.pkl

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
