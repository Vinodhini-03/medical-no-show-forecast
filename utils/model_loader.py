"""
Model Loading Utilities
Loads saved ML models and metadata for Streamlit app
"""

import joblib
import os
import pandas as pd
import numpy as np

class ModelLoader:
    """Load and manage ML models"""
    
    def __init__(self, models_dir='models'):
        self.models_dir = models_dir
        self.classifier = None
        self.forecaster = None
        self.classifier_features = None
        self.forecaster_features = None
        self.classifier_metadata = None
        self.forecaster_metadata = None
        
    def load_classifier(self):
        """Load the no-show classification model"""
        try:
            self.classifier = joblib.load(os.path.join(self.models_dir, 'best_noshow_classifier.joblib'))
            self.classifier_features = joblib.load(os.path.join(self.models_dir, 'feature_names.joblib'))
            self.classifier_metadata = joblib.load(os.path.join(self.models_dir, 'model_metadata.joblib'))
            return True
        except Exception as e:
            print(f"Error loading classifier: {e}")
            return False
    
    def load_forecaster(self):
        """Load the demand forecasting model"""
        try:
            self.forecaster = joblib.load(os.path.join(self.models_dir, 'best_demand_forecaster.joblib'))
            self.forecaster_features = joblib.load(os.path.join(self.models_dir, 'forecasting_feature_names.joblib'))
            self.forecaster_metadata = joblib.load(os.path.join(self.models_dir, 'forecasting_metadata.joblib'))
            return True
        except Exception as e:
            print(f"Error loading forecaster: {e}")
            return False
    
    def predict_noshow(self, input_data):
        """
        Predict no-show probability
        
        Args:
            input_data: DataFrame with patient features
            
        Returns:
            probability of no-show (0-1)
        """
        if self.classifier is None:
            raise ValueError("Classifier not loaded. Call load_classifier() first.")
        
        # Get prediction probability
        proba = self.classifier.predict_proba(input_data)[0]
        
        return {
            'show_probability': proba[0],
            'noshow_probability': proba[1],
            'prediction': 'No-Show Risk' if proba[1] > 0.5 else 'Likely to Show'
        }
    
    def forecast_demand(self, input_data):
        """
        Forecast daily appointment demand
        
        Args:
            input_data: DataFrame with temporal features
            
        Returns:
            predicted appointment count
        """
        if self.forecaster is None:
            raise ValueError("Forecaster not loaded. Call load_forecaster() first.")
        
        # Get prediction
        prediction = self.forecaster.predict(input_data)[0]
        
        return {
            'predicted_appointments': max(0, int(round(prediction))),  # No negative predictions
            'lower_bound': max(0, int(round(prediction - 80))),  # Based on MAE
            'upper_bound': int(round(prediction + 80))
        }