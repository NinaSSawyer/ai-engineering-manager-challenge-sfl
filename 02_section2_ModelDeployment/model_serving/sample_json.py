#extracting a single image from the test set to write to JSON--use to test Flask API
import json
import numpy as np
from tensorflow.keras.datasets import fashion_mnist

#Load the test data from Fashion MNIST
(_, _), (x_test, _) = fashion_mnist.load_data()

#Select the first sample image from the test set
sample_image = x_test[0].tolist()  # Convert numpy array to nested Python list

#Wrap the sample image in a dictionary with the key expected by the API
sample_data = {"image": sample_image}

# Save the JSON file in the current folder
with open("predict_example.json", "w") as f:
    json.dump({"image": sample_image}, f)

print("Sample JSON written to predict_example.json")