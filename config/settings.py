"""
Configuration settings and constants for FamilyAIDoc application.
"""

# Model paths
MODEL_PATHS = {
    'kidney': {
        'model': 'models/kidney/kidney_extratrees_basic.pkl',
        'scaler': 'models/kidney/kidney_extratrees_scaler.pkl',
        'metadata': 'models/kidney/kidney_extratrees_metadata.pkl',
    },
    'liver': {
        'model': 'models/liver/liver_randomforest_basic.pkl',
        'scaler': 'models/liver/liver_randomforest_scaler.pkl',
    },
    'parkinsons': {
        'model': 'models/parkinsons/parkinsons_xgboost_basic.pkl',
        'scaler': 'models/parkinsons/parkinsons_xgboost_scaler.pkl',
        'features': 'models/parkinsons/parkinsons_xgboost_features.pkl',
    }
}

# Page configuration
PAGE_CONFIG = {
    'page_title': "FamilyAIDoc - AI Disease Detection",
    'page_icon': "🏥",
    'layout': "wide",
    'initial_sidebar_state': "expanded"
}

# Navigation pages
PAGES = [
    "🏠 Home",
    "🫘 Kidney Disease",
    "🫀 Liver Disease",
    "🧠 Parkinson's Disease",
    "Medical Chatbot",
    "📊 About Models"
]

# Model information
MODEL_INFO = {
    'kidney': {
        'name': 'Chronic Kidney Disease',
        'icon': '🫘',
        'features': 24,
        'algorithm': 'Extra Trees',
        'accuracy': '100%',
    },
    'liver': {
        'name': 'Liver Disease',
        'icon': '🫀',
        'features': 10,
        'algorithm': 'Random Forest',
        'accuracy': '70%',
    },
    'parkinsons': {
        'name': "Parkinson's Disease",
        'icon': '🧠',
        'features': 22,
        'algorithm': 'XGBoost',
        'accuracy': '92.31%',
    }
}

# Parkinson's voice features
PARKINSONS_FEATURES = [
    'mdvp_fo', 'mdvp_fhi', 'mdvp_flo',
    'mdvp_jitter_percent', 'mdvp_jitter_abs', 'mdvp_rap', 'mdvp_ppq', 'jitter_ddp',
    'mdvp_shimmer', 'mdvp_shimmer_db', 'shimmer_apq3', 'shimmer_apq5',
    'mdvp_apq', 'shimmer_dda', 'nhr', 'hnr',
    'rpde', 'dfa', 'spread1', 'spread2', 'd2', 'ppe'
]

# Clinical thresholds for kidney disease
KIDNEY_THRESHOLDS = {
    'high_creatinine': 1.8,
    'high_albumin': 3,
    'high_urea': 50,
    'high_glucose': 150,
}

# Kidney disease encoding
KIDNEY_ENCODING = {
    'rbc': {'abnormal': 0, 'normal': 1},
    'pc': {'abnormal': 0, 'normal': 1},
    'pcc': {'present': 1, 'notpresent': 0},
    'ba': {'present': 1, 'notpresent': 0},
    'htn': {'yes': 1, 'no': 0},
    'dm': {'yes': 1, 'no': 0},
    'cad': {'yes': 1, 'no': 0},
    'appet': {'poor': 1, 'good': 0},
    'pe': {'yes': 1, 'no': 0},
    'ane': {'yes': 1, 'no': 0},
}

# SG values for kidney disease
SG_VALUES = [1.005, 1.010, 1.015, 1.020, 1.025]
