# Section 2 – ML Model Deployment #

This section demonstrates deployment of a machine learning model (Fashion MNIST) as an API service using Flask and Docker.

## Tools & Technologies ##

- Python 3.10
- scikit-learn
- Flask
- Docker

## Getting Started ## 

### 1. Train the Model ###

```
bash
pip install -r requirements.txt
python model_training.py
```

This script downloads Fashion MNIST data, trains a simple classifier, and saves the model to disk.

### 2. Run the Inference API (Docker) ###

```
cd model_serving
docker build -t model-api .
docker run -p 5000:5000 model-api
```

The API will be available at:
http://localhost:5000/predict

### 3. Example Request ###

Use a tool like Postman or curl:

```
curl -X POST -H "Content-Type: application/json" \
-d @predict_example.json \
http://localhost:5000/predict
```

** Files **

* model_training.py – Model pipeline and persistence
* model_serving/app.py – Flask API endpoint
* model_serving/Dockerfile – Container definition
* predict_example.json – Sample payload
* requirements.txt – Python dependencies