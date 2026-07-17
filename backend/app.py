from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to AI-Based Student Performance Prediction System"
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    study_hours = float(data.get("study_hours", 0))
    attendance = float(data.get("attendance", 0))
    previous_marks = float(data.get("previous_marks", 0))

    # Temporary prediction logic
    if study_hours >= 5 and attendance >= 75 and previous_marks >= 60:
        prediction = "Excellent Performance"
    else:
        prediction = "Needs Improvement"

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
