from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
import numpy as np

app = Flask(__name__)

#Charger le modèle entraîné
model = keras.models.loadmodel('mnistmodel.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Vérification des données
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    image_data = np.array(data['image'])
    # Assurez-vous que l’image est au bon format (1, 784) et normalisée
    imagedata = imagedata.reshape(1, 784)
    imagedata = imagedata.astype("float32") / 255.0

    prediction = model.predict(image_data)
    predicted_class = int(np.argmax(prediction, axis=1)[0])

    return jsonify({
        'prediction': predicted_class,
        'probabilities': prediction.tolist()
    })

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)
