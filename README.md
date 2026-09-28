# ChurnGuard — Telecom Churn Intelligence

A professional web interface for predicting customer churn risk using a deployed machine learning API.

ChurnGuard allows users to enter customer demographics, subscribed services, contract information, and billing details, then receive a real-time churn probability, risk segment, and recommended intervention.

## Live Demo

**Frontend:**
https://ahmeda4f.github.io/telecom-churn-frontend/


## Overview

The frontend communicates with a deployed FastAPI backend through a REST API.

```text
Customer Information
        │
        ▼
   ChurnGuard UI
        │
        │ POST /predict
        ▼
    FastAPI API
        │
        ▼
  ML Prediction Pipeline
        │
        ▼
Churn Probability
        │
        ├── Risk Segment
        │
        └── Intervention Recommendation
```

## Features

* Customer profile input
* Telecom service configuration
* Contract and billing information
* Real-time ML prediction
* Churn probability visualization
* Risk classification
* Retention intervention recommendation
* Responsive design for desktop and mobile
* REST API integration
* Static deployment through GitHub Pages

## Tech Stack

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* Google Fonts
* Fetch API

### Backend

* Python
* FastAPI
* scikit-learn
* Pandas
* Joblib

## API

The frontend sends customer information to:

```text
POST https://telecom-churn-api-6d4a060a.fastapicloud.dev/predict
```

Example request:

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 80.5,
  "TotalCharges": 402.5
}
```

Example response:

```json
{
  "churn_probability": 0.8866,
  "risk_segment": "High Risk",
  "intervention_recommended": true
}
```

## Project Structure

```text
telecom-churn-frontend/
│
├── index.html
├── style.css
├── app.js
└── README.md
```

## Deployment

This project is designed to be deployed using GitHub Pages.

## Machine Learning

The frontend does not contain the trained model.

The model is loaded and executed by the backend API. This keeps the ML pipeline on the server and allows the frontend to remain a lightweight static website.

## Project Goal

The project demonstrates an end-to-end machine learning application:

* Data preprocessing
* Exploratory data analysis
* Feature engineering
* Model training
* Model evaluation
* ML pipeline serialization
* REST API development
* Model deployment
* Frontend/API integration
* Production-style prediction workflow

## License

This project is intended for educational and portfolio purposes.
