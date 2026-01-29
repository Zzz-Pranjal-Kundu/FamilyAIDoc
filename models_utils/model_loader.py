"""
Model loading utilities for FamilyAIDoc.
Handles loading of trained models and scalers from disk.
"""

import streamlit as st
import joblib
from config.settings import MODEL_PATHS


@st.cache_resource
def load_model(model_path):
    """
    Load a model from disk with caching.
    
    Args:
        model_path (str): Path to the model file
        
    Returns:
        object: Loaded model or None if loading fails
    """
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.warning(f"Error loading {model_path}: {str(e)}")
        return None


def load_kidney_models():
    """Load kidney disease models and scaler."""
    model = load_model(MODEL_PATHS['kidney']['model'])
    scaler = load_model(MODEL_PATHS['kidney']['scaler'])
    return model, scaler


def load_liver_models():
    """Load liver disease models and scaler."""
    model = load_model(MODEL_PATHS['liver']['model'])
    scaler = load_model(MODEL_PATHS['liver']['scaler'])
    return model, scaler


def load_parkinsons_models():
    """Load Parkinson's disease models and scaler."""
    model = load_model(MODEL_PATHS['parkinsons']['model'])
    scaler = load_model(MODEL_PATHS['parkinsons']['scaler'])
    features_list = load_model(MODEL_PATHS['parkinsons']['features'])
    return model, scaler, features_list
