from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

class MedicalSymptomChecker:
    def __init__(self):
        self.model = DiscreteBayesianNetwork()
        self._build_network()
        self._define_cpds()
        self.inference = VariableElimination(self.model)
    
    def _build_network(self):
        """Build the Bayesian Network structure"""
        # Disease is the parent node, all symptoms are children
        self.model.add_node('Disease')
        symptoms = ['Fever', 'Cough', 'Fatigue', 'RunnyNose', 'BodyAches', 'Sneezing', 'SoreThroat', 'Headache']
        
        for symptom in symptoms:
            self.model.add_edge('Disease', symptom)
    
    def _define_cpds(self):
        """Define Conditional Probability Distributions"""
        
        # Disease prior probabilities
        cpd_disease = TabularCPD(
            variable='Disease',
            variable_card=5,
            values=[[0.30], [0.20], [0.25], [0.15], [0.10]],  # Cold, Flu, Allergy, COVID-19, StrepThroat
            state_names={'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Fever CPD
        cpd_fever = TabularCPD(
            variable='Fever',
            variable_card=2,
            values=[
                [0.70, 0.10, 0.95, 0.20, 0.30],  # No Fever
                [0.30, 0.90, 0.05, 0.80, 0.70]   # Fever
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'Fever': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Cough CPD
        cpd_cough = TabularCPD(
            variable='Cough',
            variable_card=2,
            values=[
                [0.20, 0.30, 0.80, 0.10, 0.40],  # No Cough
                [0.80, 0.70, 0.20, 0.90, 0.60]   # Cough
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'Cough': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Fatigue CPD
        cpd_fatigue = TabularCPD(
            variable='Fatigue',
            variable_card=2,
            values=[
                [0.40, 0.10, 0.70, 0.15, 0.50],  # No Fatigue
                [0.60, 0.90, 0.30, 0.85, 0.50]   # Fatigue
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'Fatigue': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Runny Nose CPD
        cpd_runnynose = TabularCPD(
            variable='RunnyNose',
            variable_card=2,
            values=[
                [0.20, 0.40, 0.10, 0.30, 0.60],  # No Runny Nose
                [0.80, 0.60, 0.90, 0.70, 0.40]   # Runny Nose
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'RunnyNose': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Body Aches CPD
        cpd_bodyaches = TabularCPD(
            variable='BodyAches',
            variable_card=2,
            values=[
                [0.70, 0.05, 0.80, 0.20, 0.60],  # No Body Aches
                [0.30, 0.95, 0.20, 0.80, 0.40]   # Body Aches
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'BodyAches': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Sneezing CPD
        cpd_sneezing = TabularCPD(
            variable='Sneezing',
            variable_card=2,
            values=[
                [0.30, 0.60, 0.05, 0.70, 0.80],  # No Sneezing
                [0.70, 0.40, 0.95, 0.30, 0.20]   # Sneezing
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'Sneezing': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Sore Throat CPD
        cpd_sorethroat = TabularCPD(
            variable='SoreThroat',
            variable_card=2,
            values=[
                [0.60, 0.50, 0.70, 0.40, 0.05],  # No Sore Throat
                [0.40, 0.50, 0.30, 0.60, 0.95]   # Sore Throat
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'SoreThroat': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Headache CPD
        cpd_headache = TabularCPD(
            variable='Headache',
            variable_card=2,
            values=[
                [0.50, 0.20, 0.60, 0.20, 0.40],  # No Headache
                [0.50, 0.80, 0.40, 0.80, 0.60]   # Headache
            ],
            evidence=['Disease'],
            evidence_card=[5],
            state_names={'Headache': ['No', 'Yes'], 'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']}
        )
        
        # Add all CPDs to the model
        self.model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, 
                           cpd_runnynose, cpd_bodyaches, cpd_sneezing, 
                           cpd_sorethroat, cpd_headache)
        
        # Check if the model is valid
        assert self.model.check_model()
    
    def diagnose(self, symptoms):
        """
        Diagnose based on observed symptoms
        
        Args:
            symptoms (dict): Dictionary with symptom names as keys and 'Yes'/'No' as values
        
        Returns:
            dict: Disease probabilities and most likely disease
        """
        evidence = {}
        for symptom, value in symptoms.items():
            if symptom in ['Fever', 'Cough', 'Fatigue', 'RunnyNose', 'BodyAches', 'Sneezing', 'SoreThroat', 'Headache']:
                evidence[symptom] = value
        
        # Query the model
        query_result = self.inference.query(variables=['Disease'], evidence=evidence)
        
        # Extract probabilities
        disease_states = ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat']
        probabilities = {}
        
        for i, disease in enumerate(disease_states):
            probabilities[disease] = float(query_result.values[i] * 100)
        
        # Find most likely disease
        most_likely_disease = max(probabilities, key=probabilities.get)
        max_probability = probabilities[most_likely_disease]
        
        return {
            'most_likely_disease': most_likely_disease,
            'probability': round(max_probability, 2),
            'all_probabilities': {k: round(v, 2) for k, v in probabilities.items()}
        }
    
    def get_model_info(self):
        """Get information about the model"""
        return {
            'nodes': self.model.nodes(),
            'edges': self.model.edges(),
            'cpds': [cpd.variable for cpd in self.model.cpds],
            'diseases': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat'],
            'symptoms': ['Fever', 'Cough', 'Fatigue', 'RunnyNose', 'BodyAches', 'Sneezing', 'SoreThroat', 'Headache']
        }
