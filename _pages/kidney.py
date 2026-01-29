import streamlit as st
import numpy as np
from components.gauges import create_confidence_gauge
from models_utils.model_loader import load_kidney_models
from models_utils.sample_data import KIDNEY_DISEASE_SAMPLE, KIDNEY_HEALTHY_SAMPLE
from config.settings import SG_VALUES, KIDNEY_ENCODING
from utils.encoding import encode_kidney_features
from utils.prediction_helper import assess_kidney_disease_risk, get_kidney_ckd_status


def render_kidney_page():
    """Render the kidney disease prediction page."""
    st.title("🫘 Chronic Kidney Disease Prediction")
    st.markdown("Enter the patient's clinical parameters to predict Chronic Kidney Disease (CKD)")
    
    # Load model
    model, scaler = load_kidney_models()
    
    if model is None or scaler is None:
        st.error("⚠️ Model not found! Please train the model first by running `python training_scripts/train_kidney_extratrees.py`")
    else:
        st.markdown('<div class="info-box">✅ Model loaded successfully! Extra Trees Classifier with 100% accuracy</div>', unsafe_allow_html=True)
        
        # Sample Data Buttons
        st.markdown("### 🎯 Quick Test")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            use_sample_ckd = st.button("📊 Load Sample: CKD Patient", use_container_width=True)
        with col_btn2:
            use_sample_healthy = st.button("📊 Load Sample: Healthy Patient", use_container_width=True)
        
        # Initialize session state for values
        if 'kidney_values' not in st.session_state:
            st.session_state.kidney_values = {}
        
        # Load sample data
        if use_sample_ckd:
            st.session_state.kidney_values = KIDNEY_DISEASE_SAMPLE
            st.success("✅ Loaded sample CKD patient data")
        
        if use_sample_healthy:
            st.session_state.kidney_values = KIDNEY_HEALTHY_SAMPLE
            st.success("✅ Loaded sample healthy patient data")
        
        st.markdown("---")
        
        # Input form
        st.subheader("Basic Information")
        age = st.number_input("Age (years) 👤", 1, 120, 
                            st.session_state.kidney_values.get('age', 50),
                            help="Patient's age in years")
        bp = st.number_input("Blood Pressure (mm/Hg) 🫀", 50, 200, 
                           st.session_state.kidney_values.get('bp', 80),
                           help="Blood pressure measurement")
        sg = st.selectbox("Specific Gravity 💧", SG_VALUES,
                        index=SG_VALUES.index(st.session_state.kidney_values.get('sg', 1.020)),
                        help="Urine specific gravity")
        sg_enc = SG_VALUES.index(sg)
        al = st.selectbox("Albumin 🧪", [0, 1, 2, 3, 4, 5],
                        index=st.session_state.kidney_values.get('al', 0),
                        help="Albumin level in urine")
        su = st.selectbox("Sugar 🍬", [0, 1, 2, 3, 4, 5],
                        index=st.session_state.kidney_values.get('su', 0),
                        help="Sugar level in urine")
        rbc = st.selectbox("Red Blood Cells 🔴", ["normal", "abnormal"],
                         index=0 if st.session_state.kidney_values.get('rbc', 'normal')=='normal' else 1,
                         help="RBC in urine test")
        pc = st.selectbox("Pus Cell 🦠", ["normal", "abnormal"],
                        index=0 if st.session_state.kidney_values.get('pc', 'normal')=='normal' else 1,
                        help="Pus cells in urine")
        pcc = st.selectbox("Pus Cell Clumps 🧫", ["present", "notpresent"],
                         index=0 if st.session_state.kidney_values.get('pcc', 'notpresent')=='present' else 1,
                         help="Presence of pus cell clumps")
        ba = st.selectbox("Bacteria 🦠", ["present", "notpresent"],
                        index=0 if st.session_state.kidney_values.get('ba', 'notpresent')=='present' else 1,
                        help="Bacteria in urine")
        
        st.subheader("Blood Tests")
        bgr = st.number_input("Blood Glucose Random (mgs/dl) 🩸", 20, 500, 
                            st.session_state.kidney_values.get('bgr', 120),
                            help="Random blood glucose level")
        bu = st.number_input("Blood Urea (mgs/dl) 🧬", 1, 400, 
                           st.session_state.kidney_values.get('bu', 40),
                           help="Blood urea measurement")
        sc = st.number_input("Serum Creatinine (mgs/dl) ⚗️", 0.1, 20.0, 
                           float(st.session_state.kidney_values.get('sc', 1.2)), 0.1,
                           help="Serum creatinine level")
        sod = st.number_input("Sodium (mEq/L) 🧂", 50, 200, 
                            st.session_state.kidney_values.get('sod', 140),
                            help="Sodium level in blood")
        pot = st.number_input("Potassium (mEq/L) 🥔", 1.0, 20.0, 
                            float(st.session_state.kidney_values.get('pot', 4.5)), 0.1,
                            help="Potassium level in blood")
        hemo = st.number_input("Hemoglobin (gms) 🩸", 1.0, 20.0, 
                             float(st.session_state.kidney_values.get('hemo', 14.0)), 0.1,
                             help="Hemoglobin count")
        pcv = st.number_input("Packed Cell Volume 📊", 10, 60, 
                            st.session_state.kidney_values.get('pcv', 40),
                            help="Packed cell volume percentage")
        
        st.subheader("Additional Parameters")
        wc = st.number_input("White Blood Cell Count (cells/cumm) ⚪", 1000, 30000, 
                           st.session_state.kidney_values.get('wc', 8000),
                           help="WBC count")
        rc = st.number_input("Red Blood Cell Count (millions/cmm) 🔴", 1.0, 10.0, 
                           float(st.session_state.kidney_values.get('rc', 4.5)), 0.1,
                           help="RBC count")
        htn = st.selectbox("Hypertension 💔", ["yes", "no"],
                         index=0 if st.session_state.kidney_values.get('htn', 'no')=='yes' else 1,
                         help="History of hypertension")
        dm = st.selectbox("Diabetes Mellitus 🍭", ["yes", "no"],
                        index=0 if st.session_state.kidney_values.get('dm', 'no')=='yes' else 1,
                        help="History of diabetes")
        cad = st.selectbox("Coronary Artery Disease 🫀", ["yes", "no"],
                         index=0 if st.session_state.kidney_values.get('cad', 'no')=='yes' else 1,
                         help="Coronary artery disease history")
        appet = st.selectbox("Appetite 🍽️", ["good", "poor"],
                           index=0 if st.session_state.kidney_values.get('appet', 'good')=='good' else 1,
                           help="Patient's appetite")
        pe = st.selectbox("Pedal Edema 🦶", ["yes", "no"],
                        index=0 if st.session_state.kidney_values.get('pe', 'no')=='yes' else 1,
                        help="Swelling in feet")
        ane = st.selectbox("Anemia 🩸", ["yes", "no"],
                         index=0 if st.session_state.kidney_values.get('ane', 'no')=='yes' else 1,
                         help="Presence of anemia")
        
        if st.button("🔍 Predict Kidney Disease", type="primary"):
            # Encode categorical variables
            rbc_enc, pc_enc, pcc_enc, ba_enc, htn_enc, dm_enc, cad_enc, appet_enc, pe_enc, ane_enc = encode_kidney_features(
                rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane
            )
            
            # Create feature array
            features = np.array([[age, bp, sg_enc, al, su, rbc_enc, pc_enc, pcc_enc, ba_enc, bgr, 
                                bu, sc, sod, pot, hemo, pcv, wc, rc, htn_enc, dm_enc, cad_enc, 
                                appet_enc, pe_enc, ane_enc]])
            
            # Scale and predict
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
            prediction_proba = model.predict_proba(features_scaled)[0]
            
            st.markdown("---")
            st.subheader("📊 Prediction Result")
            
            confidence = prediction_proba[prediction]*100
            
            # Display confidence gauge
            col_gauge, col_result = st.columns([1, 1])
            
            with col_gauge:
                fig = create_confidence_gauge(confidence, "Prediction Confidence")
                st.plotly_chart(fig, use_container_width=True)
            
            with col_result:
                # Determine CKD status
                ckd_detected = get_kidney_ckd_status(model, prediction)
                
                # Clinical risk assessment
                risk_override, override_reasons = assess_kidney_disease_risk(
                    rbc, pc, pcc, pe, ane, sc, al, bu, bgr
                )
                
                if ckd_detected or risk_override:
                    st.markdown(f'<div class="gradient-card"><h2>⚠️ Chronic Kidney Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                    st.warning("⚠️ **Recommendation:** Immediate consultation with a nephrologist is advised.")
                else:
                    st.markdown(f'<div class="success-box"><h2>✅ No Chronic Kidney Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                    st.info("💡 **Recommendation:** Maintain a healthy lifestyle and regular checkups.")
