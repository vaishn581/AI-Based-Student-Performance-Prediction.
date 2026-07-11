# 🎓 AI-Based Student Performance Prediction

An AI-powered web application that predicts student academic performance based on factors such as attendance, study hours, previous grades, assignments, and other academic information.

The project uses Machine Learning with a Flask backend and a responsive HTML, CSS, and JavaScript frontend to provide predictions through REST APIs.

---

# 📖 Introduction

Student performance prediction is an important application of Artificial Intelligence in education. This project helps educational institutions analyze student data and predict academic performance, allowing teachers and students to identify learning gaps early.

The application demonstrates the integration of Machine Learning models with a Flask web application using a Client-Server architecture.

---

# 📌 Project Overview

This project predicts whether a student is likely to perform well based on academic data.

The system:
- Collects student information
- Processes the data
- Uses a trained Machine Learning model
- Predicts student performance
- Displays the result through a web interface

---

# 📌 Features

- Student Performance Prediction
- User-friendly Interface
- Machine Learning Model
- Flask REST API
- JSON Communication
- Data Processing
- Responsive Design
- Easy Deployment
- Modular Project Structure

---

# 🏗️ System Architecture

```
+----------------------+
|      Frontend        |
| HTML • CSS • JS      |
+----------+-----------+
           |
           | HTTP Request
           |
+----------v-----------+
|     Flask Backend    |
|       app.py         |
+----------+-----------+
           |
           | Prediction Request
           |
+----------v-----------+
| Machine Learning     |
| Prediction Model     |
+----------+-----------+
           |
           |
+----------v-----------+
| Prediction Result    |
+----------------------+
```

---

# 🔄 Workflow

1. User enters student details.
2. Frontend sends data to Flask API.
3. Flask validates the input.
4. Machine Learning model processes the data.
5. Prediction is generated.
6. Flask returns JSON response.
7. Frontend displays predicted performance.

---

# 📡 API Endpoints

## Home

**GET /**

Returns welcome message.

Example Response

```json
{
  "message":"Welcome to Student Performance Prediction System"
}
```

---

## Predict Student Performance

**POST /predict**

Request

```json
{
  "study_hours":5,
  "attendance":90,
  "previous_marks":82
}
```

Response

```json
{
  "prediction":"Excellent Performance"
}
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Based-Student-Performance-Prediction.git
```

```bash
cd AI-Based-Student-Performance-Prediction
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

---

# 📂 Folder Structure

```
AI-Based-Student-Performance-Prediction/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── model/
│   └── student_model.pkl
│
├── src/
│   ├── app.py
│   ├── predict.py
│   └── train_model.py
│
├── data/
│   ├── student_data.csv
│
├── deployment/
│
├── diagrams/
│
├── documents/
│
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📑 Documentation

The project documentation contains:

- Project Report
- Machine Learning Documentation
- API Documentation
- System Architecture
- Workflow Diagram
- Installation Guide

---

# ⚙️ Working

- User enters student details.
- Data is sent to Flask backend.
- Backend preprocesses the input.
- Machine Learning model predicts performance.
- Prediction is returned to frontend.
- Result is displayed instantly.

---

# 📊 Data Source Documentation

The project uses student academic datasets containing:

- Study Hours
- Attendance
- Assignment Scores
- Previous Marks
- Internal Assessment
- Final Grade

Dataset can be collected from educational institutions or public educational datasets.

---

# 💡 Uses

- Schools
- Colleges
- Student Performance Analysis
- Academic Monitoring
- Early Risk Detection
- Machine Learning Learning Project
- Flask API Practice
- Internship Project

---

# 👥 Team Members

| Role | Responsibility |
|------|----------------|
| Developer | Frontend Development |
| Developer | Backend Development |
| Developer | Machine Learning |
| Developer | Documentation |

---

# 🔮 Future Enhancements

- Deep Learning Model
- Student Dashboard
- Login Authentication
- Database Integration
- Email Notifications
- Performance Analytics
- Data Visualization
- Cloud Deployment

---

# 📜 License

This project is developed for educational and learning purposes.

---

# 🙏 Acknowledgements

- Python Community
- Flask Framework
- Scikit-Learn
- Pandas
- NumPy
- HTML CSS JavaScript Community
- Open Source Contributors

---

---

# 📅 Internship Timeline

## Week 1
- Repository Setup
- Folder Structure
- Documentation

## Week 2
- Dataset Collection
- Data Preprocessing

## Week 3
- Machine Learning Model Development

## Week 4
- Model Training & Evaluation

## Week 5
- Performance Comparison
- Report Writing

## Week 6
- Final Presentation
- Project Demonstration

---

# 👩‍💻 Developed By

**Vaishnavi Langote**

B.Tech Computer Science Engineering

U2UInnovate Internship 2026


# ✅ Conclusion

The AI-Based Student Performance Prediction System demonstrates the practical application of Machine Learning in education. It helps educators identify students who may need additional support while providing a simple example of integrating Machine Learning with Flask REST APIs.

The project is suitable for internships, academic demonstrations, and beginner-level AI application development.

