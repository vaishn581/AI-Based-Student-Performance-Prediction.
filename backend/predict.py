import joblib
import numpy as np

# Load trained model
model = joblib.load("../model/student_model.pkl")

def predict_performance(study_hours, attendance, previous_marks):

    data = np.array([[study_hours, attendance, previous_marks]])

    prediction = model.predict(data)

    return prediction[0]
