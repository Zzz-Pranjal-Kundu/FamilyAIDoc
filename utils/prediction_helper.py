"""
Helper functions for disease predictions and clinical assessments.
"""

from config.settings import KIDNEY_THRESHOLDS


def assess_kidney_disease_risk(rbc, pc, pcc, pe, ane, sc, al, bu, bgr):
    """
    Assess clinical risk factors for kidney disease.
    
    Args:
        rbc (str): Red Blood Cells status
        pc (str): Pus Cell status
        pcc (str): Pus Cell Clumps status
        pe (str): Pedal Edema status
        ane (str): Anemia status
        sc (float): Serum Creatinine
        al (int): Albumin level
        bu (float): Blood Urea
        bgr (float): Blood Glucose Random
        
    Returns:
        tuple: (risk_override, override_reasons)
    """
    override_reasons = []
    
    high_creatinine = (sc >= KIDNEY_THRESHOLDS['high_creatinine'])
    high_albumin = (al >= KIDNEY_THRESHOLDS['high_albumin'])
    high_urea = (bu >= KIDNEY_THRESHOLDS['high_urea'])
    high_glucose = (bgr >= KIDNEY_THRESHOLDS['high_glucose'])
    
    rbc_abnormal = (rbc == 'abnormal')
    pc_abnormal = (pc == 'abnormal')
    pcc_present = (pcc == 'present')
    pe_present = (pe == 'yes')
    ane_present = (ane == 'yes')
    
    if high_creatinine:
        override_reasons.append('Serum Creatinine ≥ 1.8 mg/dL')
    if high_albumin:
        override_reasons.append('Urine Albumin ≥ 3')
    if rbc_abnormal and pc_abnormal:
        override_reasons.append('Abnormal RBC and Pus Cells')
    if pcc_present:
        override_reasons.append('Pus Cell Clumps present')
    if pe_present:
        override_reasons.append('Pedal Edema present')
    if ane_present:
        override_reasons.append('Anemia present')
    if high_urea:
        override_reasons.append('Blood Urea ≥ 50 mg/dL')
    if high_glucose:
        override_reasons.append('Random Blood Glucose ≥ 150 mg/dL')
    
    risk_override = (
        high_creatinine and (high_albumin or rbc_abnormal or pc_abnormal or pcc_present)
    ) or (
        high_creatinine and (pe_present or ane_present)
    ) or (
        high_creatinine and high_urea
    )
    
    return risk_override, override_reasons


def get_kidney_ckd_status(model, prediction):
    """
    Determine CKD status from model prediction.
    
    Args:
        model: Trained model
        prediction (int): Predicted class
        
    Returns:
        bool: True if CKD detected, False otherwise
    """
    # Try to load metadata for accurate mapping
    try:
        import joblib
        meta = joblib.load('models/kidney/kidney_extratrees_metadata.pkl')
        if isinstance(meta, dict) and 'target_classes' in meta:
            text_classes = [str(c).strip().lower().replace('\t', '').replace(' ', '') 
                           for c in meta['target_classes']]
            ckd_indices = [i for i, c in enumerate(text_classes) 
                          if c in ('ckd', 'chronickidneydisease')]
            if ckd_indices:
                return int(prediction) in ckd_indices
    except:
        pass
    
    # Fallback logic
    if hasattr(model, 'classes_') and len(getattr(model, 'classes_', [])) == 3:
        return int(prediction) in [0, 1]
    
    return int(prediction) == 0
