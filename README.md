# Medical Symptom Checker - Bayesian Network Web App

A web application that uses Bayesian Networks to diagnose common illnesses based on symptoms.

## 🎯 Project Overview

This application demonstrates Bayesian Network concepts through a practical medical diagnosis system. It analyzes symptoms and calculates the probability of different diseases using probabilistic inference.

### Features
- **5 Diseases**: Cold, Flu, Allergy, COVID-19, Strep Throat
- **8 Symptoms**: Fever, Cough, Fatigue, Runny Nose, Body Aches, Sneezing, Sore Throat, Headache
- **Real-time Inference**: Uses Bayesian Network for probabilistic reasoning
- **Interactive UI**: Visual symptom selection and probability visualization
- **Educational**: Shows how Bayesian Networks work in practice

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

The app will start at: **http://localhost:5000**

## 📁 Project Structure

```
bayesian-medical-app/
├── app.py                 # Flask web application
├── bayesian_model.py      # Bayesian Network model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
└── README.md             # This file
```

## 🎓 How It Works

### Bayesian Network Structure

```
Disease (Prior: Cold=30%, Flu=20%, Allergy=25%, COVID-19=15%, StrepThroat=10%)
   ├── Fever
   ├── Cough
   ├── Fatigue
   ├── RunnyNose
   ├── BodyAches
   ├── Sneezing
   ├── SoreThroat
   └── Headache
```

### Inference Process

1. User selects observed symptoms
2. Bayesian Network uses Variable Elimination algorithm
3. Calculates posterior probabilities for each disease
4. Returns diagnosis with confidence scores

## 🧪 Test Cases

The application includes built-in test cases to demonstrate different scenarios:
- **COVID-19**: Fever + Cough + Body Aches + Fatigue + Headache
- **Flu**: Fever + Body Aches + Fatigue + Headache (no cough)
- **Allergy**: Sneezing + Runny Nose (no fever)
- **Strep Throat**: Severe Sore Throat + Fever
- **Cold**: Cough + Runny Nose + Sneezing + Sore Throat

## 📊 API Endpoints

### GET `/`
Returns the main HTML interface

### POST `/diagnose`
**Request Body**:
```json
{
  "Fever": "Yes",
  "Cough": "Yes",
  "Fatigue": "Yes",
  "RunnyNose": "No",
  "BodyAches": "Yes",
  "Sneezing": "No",
  "SoreThroat": "No",
  "Headache": "Yes"
}
```

**Response**:
```json
{
  "success": true,
  "result": {
    "most_likely_disease": "COVID-19",
    "probability": 78.45,
    "all_probabilities": {
      "COVID-19": 78.45,
      "Flu": 15.23,
      "Cold": 4.12,
      "Allergy": 1.20,
      "StrepThroat": 1.00
    }
  }
}
```

### GET `/api/info`
Returns model information

### GET `/api/test`
Returns test cases for demonstration

## ⚠️ Disclaimer

This application is for **educational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
