# Medical Symptom Checker - Bayesian Network Web App

A web application that uses Bayesian Networks to diagnose common illnesses (Cold, Flu, Allergy) based on symptoms.

## 🎯 Project Overview

This application demonstrates Bayesian Network concepts through a practical medical diagnosis system. It analyzes symptoms and calculates the probability of different diseases using probabilistic inference.

### Features
- **5 Diseases**: Cold, Flu, Allergy, COVID-19, Strep Throat
- **8 Symptoms**: Fever, Cough, Fatigue, Runny Nose, Body Aches, Sneezing, Sore Throat, Headache
- **Real-time Inference**: Uses Bayesian Network for probabilistic reasoning
- **Interactive UI**: Visual symptom selection and probability visualization
- **Educational**: Shows how Bayesian Networks work in practice

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Quick Start (5 Minutes Setup)

### Step 1: Create Project Structure

```bash
mkdir bayesian-medical-app
cd bayesian-medical-app
```

Create the following folder structure:
```
bayesian-medical-app/
├── app.py
├── bayesian_model.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

### Step 2: Install Dependencies

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

### Step 3: Copy the Files

1. Copy `bayesian_model.py` content (the Bayesian Network model)
2. Copy `app.py` content (the Flask application)
3. Create `templates/` folder and copy `index.html` into it
4. Copy `requirements.txt` content

### Step 4: Run the Application

```bash
python app.py
```

The app will start at: **http://localhost:5000**

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

### Conditional Probabilities

Each symptom has different probabilities given each disease:

- **Flu**: High fever (90%), high body aches (95%), high fatigue (90%), high headache (80%)
- **COVID-19**: Very high cough (90%), high fever (80%), high body aches (80%), high fatigue (85%)
- **Cold**: Moderate symptoms, high runny nose (80%), high cough (80%), high sneezing (70%)
- **Allergy**: High sneezing (95%), high runny nose (90%), low fever (5%)
- **Strep Throat**: Very high sore throat (95%), high fever (70%)

### Inference Process

1. User selects observed symptoms
2. Bayesian Network uses Variable Elimination algorithm
3. Calculates posterior probabilities for each disease
4. Returns diagnosis with confidence scores

## 🧪 Test Cases

### Example 1: COVID-19 Diagnosis
**Symptoms**: Fever + Cough + Body Aches + Fatigue + Headache
**Expected**: ~70-85% COVID-19 probability

### Example 2: Flu Diagnosis
**Symptoms**: Fever + Body Aches + Fatigue + Headache (no cough)
**Expected**: ~75-85% Flu probability

### Example 3: Allergy Diagnosis
**Symptoms**: Sneezing + Runny Nose (no fever)
**Expected**: ~80-90% Allergy probability

### Example 4: Strep Throat Diagnosis
**Symptoms**: Severe Sore Throat + Fever
**Expected**: ~70-85% Strep Throat probability

### Example 5: Cold Diagnosis
**Symptoms**: Cough + Runny Nose + Sneezing + Sore Throat
**Expected**: ~60-75% Cold probability

## 🎨 Customization Ideas

### Add More Diseases
```python
# In bayesian_model.py
cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=4,  # Add Bronchitis
    values=[[0.25], [0.25], [0.25], [0.25]],
    state_names={'Disease': ['Cold', 'Flu', 'Allergy', 'Bronchitis']}
)
```

### Add More Symptoms
```python
# Add headache
self.model.add_edges_from([('Disease', 'Headache')])
```

### Adjust Probabilities
Modify the CPD values in `_define_cpds()` to match real medical data or your specific use case.

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
```

### GET `/api/info`
Returns model information

## 🐛 Troubleshooting

### Issue: pgmpy installation fails
**Solution**: Make sure you have the latest pip
```bash
pip install --upgrade pip
pip install pgmpy
```

### Issue: Port 5000 already in use
**Solution**: Change the port in app.py
```python
app.run(debug=True, port=5001)
```

### Issue: Template not found
**Solution**: Make sure `index.html` is in `templates/` folder

## 📚 Learning Resources

- **pgmpy Documentation**: https://pgmpy.org/
- **Bayesian Networks**: Understanding probabilistic graphical models
- **Flask Documentation**: https://flask.palletsprojects.com/

## 🚀 Deployment Options

### Option 1: Heroku
```bash
# Add Procfile
echo "web: python app.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Option 2: Render
1. Push to GitHub
2. Connect to Render
3. Deploy as Web Service

### Option 3: PythonAnywhere
1. Upload files
2. Configure WSGI
3. Run application

## 📝 License

Educational use - feel free to modify and extend!

## 🤝 Contributing

This is a educational project. Feel free to:
- Add more diseases
- Improve probability tables with real medical data
- Enhance the UI
- Add unit tests

## ⚠️ Disclaimer

This application is for **educational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
