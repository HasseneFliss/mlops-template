
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY model/trained_model.pkl ./model/trained_model.pkl

EXPOSE 5000
CMD ["python", "src/app.py"]
