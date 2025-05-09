#Defines the container that serves Flask app
FROM python:3.11-slim

#Set working directory inside the container
WORKDIR /app

#Copy files into the container
COPY app.py .
COPY fashion_mnist_model.h5 .
COPY requirements.txt .

#Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expose Flask default port
EXPOSE 5000

#Run the Flask app
CMD ["python", "app.py"]