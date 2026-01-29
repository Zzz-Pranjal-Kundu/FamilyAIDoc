"""
Encoding utilities for categorical variables in predictions.
"""

from config.settings import KIDNEY_ENCODING


def encode_kidney_features(rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane):
    """
    Encode categorical features for kidney disease prediction.
    
    Args:
        rbc (str): Red Blood Cells
        pc (str): Pus Cell
        pcc (str): Pus Cell Clumps
        ba (str): Bacteria
        htn (str): Hypertension
        dm (str): Diabetes Mellitus
        cad (str): Coronary Artery Disease
        appet (str): Appetite
        pe (str): Pedal Edema
        ane (str): Anemia
        
    Returns:
        tuple: Encoded feature values
    """
    return (
        KIDNEY_ENCODING['rbc'].get(rbc, 1),
        KIDNEY_ENCODING['pc'].get(pc, 1),
        KIDNEY_ENCODING['pcc'].get(pcc, 0),
        KIDNEY_ENCODING['ba'].get(ba, 0),
        KIDNEY_ENCODING['htn'].get(htn, 0),
        KIDNEY_ENCODING['dm'].get(dm, 0),
        KIDNEY_ENCODING['cad'].get(cad, 0),
        KIDNEY_ENCODING['appet'].get(appet, 0),
        KIDNEY_ENCODING['pe'].get(pe, 0),
        KIDNEY_ENCODING['ane'].get(ane, 0),
    )


def encode_gender(gender):
    """
    Encode gender for liver disease prediction.
    
    Args:
        gender (str): "Male" or "Female"
        
    Returns:
        int: Encoded value (1 for Male, 0 for Female)
    """
    return 1 if gender == "Male" else 0
