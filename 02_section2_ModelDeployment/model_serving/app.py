#Flask API that loads the model and serves predictions
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

#Load the trained model
model = tf.keras.models.load_model("fashion_mnist_model.h5")

#Define class labels (optional, for readability)
class_labels = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

#Initialize Flask app
app = Flask(__name__)

#Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        #Expecting JSON with a 28x28 array named "image"
        data = request.get_json()
        img = np.array(data['image'], dtype=np.float32)

        #Reshape and normalize input
        img = img / 255.0
        img = np.expand_dims(img, axis=(0, -1))  # shape: (1, 28, 28, 1)

        #Get prediction
        prediction = model.predict(img)
        predicted_class = int(np.argmax(prediction))
        label = class_labels[predicted_class]

        return jsonify({
            "predicted_class": predicted_class,
            "label": label,
            "confidence": float(np.max(prediction))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
