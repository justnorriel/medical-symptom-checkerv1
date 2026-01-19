from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Simplified medical symptom checker without heavy ML dependencies
class SimpleMedicalSymptomChecker:
    def __init__(self):
        self.diseases = {
            'COVID-19': {
                'symptoms': {'Fever': 0.9, 'Cough': 0.8, 'Fatigue': 0.7, 'BodyAches': 0.6, 'Headache': 0.5},
                'base_prob': 0.1
            },
            'Flu': {
                'symptoms': {'Fever': 0.8, 'Fatigue': 0.9, 'BodyAches': 0.8, 'Headache': 0.6},
                'base_prob': 0.15
            },
            'Common Cold': {
                'symptoms': {'Cough': 0.7, 'RunnyNose': 0.8, 'Sneezing': 0.6, 'SoreThroat': 0.5},
                'base_prob': 0.2
            },
            'Allergies': {
                'symptoms': {'RunnyNose': 0.9, 'Sneezing': 0.8, 'SoreThroat': 0.3},
                'base_prob': 0.25
            },
            'Strep Throat': {
                'symptoms': {'SoreThroat': 0.9, 'Fever': 0.7},
                'base_prob': 0.05
            }
        }
    
    def diagnose(self, symptoms):
        """Diagnose based on symptoms using simple probability calculation"""
        results = {}
        
        for disease, info in self.diseases.items():
            probability = info['base_prob']
            
            # Calculate probability based on present symptoms
            present_symptoms = sum(1 for symptom, value in symptoms.items() 
                                 if value == 'Yes' and symptom in info['symptoms'])
            
            if present_symptoms > 0:
                # Simple Bayesian-like calculation
                symptom_prob = 1.0
                for symptom, value in symptoms.items():
                    if value == 'Yes' and symptom in info['symptoms']:
                        symptom_prob *= info['symptoms'][symptom]
                    elif value == 'No' and symptom in info['symptoms']:
                        symptom_prob *= (1 - info['symptoms'][symptom])
                
                # Update probability
                probability *= symptom_prob * 2  # Boost factor for present symptoms
            
            results[disease] = min(probability, 0.95)  # Cap at 95%
        
        # Sort by probability
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'most_likely_disease': sorted_results[0][0] if sorted_results else 'Unknown',
            'probability': round(sorted_results[0][1] * 100) if sorted_results else 0,
            'all_probabilities': {k: round(v * 100) for k, v in sorted_results}
        }
    
    def get_model_info(self):
        """Get model information"""
        return {
            'model_type': 'Simplified Probability Model',
            'diseases': list(self.diseases.keys()),
            'symptoms': list(set(symptom for disease in self.diseases.values() 
                               for symptom in disease['symptoms'].keys())),
            'version': '1.0-lite'
        }

# Initialize the medical symptom checker
symptom_checker = SimpleMedicalSymptomChecker()

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
