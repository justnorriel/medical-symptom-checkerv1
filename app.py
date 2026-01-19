from flask import Flask, render_template, request, jsonify
from bayesian_model import MedicalSymptomChecker
import json

app = Flask(__name__)

# Initialize the medical symptom checker
symptom_checker = MedicalSymptomChecker()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    """Diagnose based on symptoms"""
    try:
        # Get symptoms from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No symptoms provided'
            }), 400
        
        # Convert symptom values to proper format
        symptoms = {}
        for symptom, value in data.items():
            if value in ['Yes', 'No']:
                symptoms[symptom] = value
        
        # Get diagnosis
        result = symptom_checker.diagnose(symptoms)
        
        return jsonify({
            'success': True,
            'result': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/info', methods=['GET'])
def get_model_info():
    """Get model information"""
    try:
        info = symptom_checker.get_model_info()
        return jsonify({
            'success': True,
            'info': info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/test', methods=['GET'])
def test_cases():
    """Get test cases for demonstration"""
    test_cases = [
        {
            'name': 'COVID-19 Case',
            'symptoms': {
                'Fever': 'Yes',
                'Cough': 'Yes',
                'Fatigue': 'Yes',
                'RunnyNose': 'No',
                'BodyAches': 'Yes',
                'Sneezing': 'No',
                'SoreThroat': 'No',
                'Headache': 'Yes'
            }
        },
        {
            'name': 'Flu Case',
            'symptoms': {
                'Fever': 'Yes',
                'Cough': 'No',
                'Fatigue': 'Yes',
                'RunnyNose': 'No',
                'BodyAches': 'Yes',
                'Sneezing': 'No',
                'SoreThroat': 'No',
                'Headache': 'Yes'
            }
        },
        {
            'name': 'Allergy Case',
            'symptoms': {
                'Fever': 'No',
                'Cough': 'No',
                'Fatigue': 'No',
                'RunnyNose': 'Yes',
                'BodyAches': 'No',
                'Sneezing': 'Yes',
                'SoreThroat': 'No',
                'Headache': 'No'
            }
        },
        {
            'name': 'Strep Throat Case',
            'symptoms': {
                'Fever': 'Yes',
                'Cough': 'No',
                'Fatigue': 'No',
                'RunnyNose': 'No',
                'BodyAches': 'No',
                'Sneezing': 'No',
                'SoreThroat': 'Yes',
                'Headache': 'No'
            }
        },
        {
            'name': 'Cold Case',
            'symptoms': {
                'Fever': 'No',
                'Cough': 'Yes',
                'Fatigue': 'No',
                'RunnyNose': 'Yes',
                'BodyAches': 'No',
                'Sneezing': 'Yes',
                'SoreThroat': 'Yes',
                'Headache': 'No'
            }
        }
    ]
    
    return jsonify({
        'success': True,
        'test_cases': test_cases
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
