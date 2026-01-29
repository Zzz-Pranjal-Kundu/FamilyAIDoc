"""
Sample data for quick testing of disease prediction models.
"""

# Kidney Disease Sample Data
KIDNEY_DISEASE_SAMPLE = {
    'age': 65, 'bp': 90, 'sg': 1.015, 'al': 4, 'su': 0, 'rbc': 'abnormal',
    'pc': 'abnormal', 'pcc': 'present', 'ba': 'notpresent', 'bgr': 150,
    'bu': 55, 'sc': 1.8, 'sod': 135, 'pot': 4.8, 'hemo': 10.5, 'pcv': 32,
    'wc': 9200, 'rc': 3.8, 'htn': 'yes', 'dm': 'yes', 'cad': 'no',
    'appet': 'poor', 'pe': 'yes', 'ane': 'yes'
}

KIDNEY_HEALTHY_SAMPLE = {
    'age': 23, 'bp': 80, 'sg': 1.025, 'al': 0, 'su': 0, 'rbc': 'normal',
    'pc': 'normal', 'pcc': 'notpresent', 'ba': 'notpresent', 'bgr': 70,
    'bu': 36, 'sc': 1.0, 'sod': 150, 'pot': 4.6, 'hemo': 17.0, 'pcv': 52,
    'wc': 9800, 'rc': 5.0, 'htn': 'no', 'dm': 'no', 'cad': 'no',
    'appet': 'good', 'pe': 'no', 'ane': 'no'
}

# Liver Disease Sample Data
LIVER_DISEASE_SAMPLE = {
    'age': 55, 'gender': 'Male',
    'total_bilirubin': 2.5, 'direct_bilirubin': 0.9,
    'alkaline_phosphotase': 280, 'alamine_aminotransferase': 120,
    'aspartate_aminotransferase': 150, 'total_protiens': 6.2,
    'albumin': 2.8, 'ag_ratio': 0.82
}

LIVER_HEALTHY_SAMPLE = {
    'age': 35, 'gender': 'Female',
    'total_bilirubin': 0.7, 'direct_bilirubin': 0.2,
    'alkaline_phosphotase': 175, 'alamine_aminotransferase': 28,
    'aspartate_aminotransferase': 32, 'total_protiens': 7.5,
    'albumin': 4.2, 'ag_ratio': 1.27
}

# Parkinson's Disease Sample Data
PARKINSONS_DISEASE_SAMPLE = {
    'mdvp_fo': 197.0, 'mdvp_fhi': 206.0, 'mdvp_flo': 192.0,
    'mdvp_jitter_percent': 0.00784, 'mdvp_jitter_abs': 0.00007,
    'mdvp_rap': 0.00370, 'mdvp_ppq': 0.00554, 'jitter_ddp': 0.01109,
    'mdvp_shimmer': 0.04374, 'mdvp_shimmer_db': 0.426, 'shimmer_apq3': 0.02182,
    'shimmer_apq5': 0.03130, 'mdvp_apq': 0.02971, 'shimmer_dda': 0.06545,
    'nhr': 0.02211, 'hnr': 21.033, 'rpde': 0.414783, 'dfa': 0.815285,
    'spread1': -4.813031, 'spread2': 0.266482, 'd2': 2.301442, 'ppe': 0.284654
}

PARKINSONS_HEALTHY_SAMPLE = {
    'mdvp_fo': 119.992, 'mdvp_fhi': 157.302, 'mdvp_flo': 74.997,
    'mdvp_jitter_percent': 0.00289, 'mdvp_jitter_abs': 0.00001,
    'mdvp_rap': 0.00166, 'mdvp_ppq': 0.00168, 'jitter_ddp': 0.00498,
    'mdvp_shimmer': 0.01888, 'mdvp_shimmer_db': 0.164, 'shimmer_apq3': 0.00954,
    'shimmer_apq5': 0.01070, 'mdvp_apq': 0.01767, 'shimmer_dda': 0.02862,
    'nhr': 0.00777, 'hnr': 26.775, 'rpde': 0.422229, 'dfa': 0.741367,
    'spread1': -7.348300, 'spread2': 0.177551, 'd2': 1.743867, 'ppe': 0.085569
}
