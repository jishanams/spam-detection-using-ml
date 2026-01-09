from flask import Flask, request, jsonify
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)  # Corrected

# Load model and scaler
model = joblib.load("spam_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract inputs in same order as training
    features = np.array([[
        data['num_links'],
        data['num_words'],
        data['has_offer'],
        data['sender_score'],
        data['all_caps']
    ]])

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)[0]

    return jsonify({
        "spam": int(prediction),
        "message": "Spam" if prediction == 1 else "Not Spam"
    })

@app.route('/', methods=['GET'])
def home():
    return "Spam Detection API is running!"

if __name__ == '__main__':  # Corrected
    app.run(debug=True)
