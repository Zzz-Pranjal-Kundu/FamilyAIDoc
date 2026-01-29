"""
Liver Disease Prediction page.
"""

import streamlit as st
import numpy as np
from components.gauges import create_confidence_gauge
from models_utils.model_loader import load_liver_models
from models_utils.sample_data import LIVER_DISEASE_SAMPLE, LIVER_HEALTHY_SAMPLE
from utils.encoding import encode_gender


def render_liver_page():
    """Render the liver disease prediction page."""
    st.title("🫀 Liver Disease Prediction")
    st.markdown("Enter the patient's liver function test parameters to predict liver disease")
    
    # Load model
    model, scaler = load_liver_models()
    
    if model is None or scaler is None:
        st.error("⚠️ Model not found! Please train the model first by running `python training_scripts/train_liver_randomforest.py`")
    else:
        st.markdown('<div class="info-box">✅ Model loaded successfully - Ready for prediction!</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Sample data buttons
        st.subheader("🧪 Quick Test Samples")
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
        with col_btn1:
            use_sample_liver = st.button("📊 Load Sample: Liver Disease Patient", use_container_width=True)
        with col_btn2:
            use_sample_healthy = st.button("📊 Load Sample: Healthy Patient", use_container_width=True)
        
        # Initialize session state
        if 'liver_values' not in st.session_state:
            st.session_state.liver_values = {}
        
        # Load sample data
        if use_sample_liver:
            st.session_state.liver_values = LIVER_DISEASE_SAMPLE
            st.success("✅ Loaded sample liver disease patient data")
        
        elif use_sample_healthy:
            st.session_state.liver_values = LIVER_HEALTHY_SAMPLE
            st.success("✅ Loaded sample healthy patient data")
        
        st.markdown("---")
        
        st.subheader("Patient Information")
        age = st.number_input("Age (years) 👤", 1, 120, value=st.session_state.liver_values.get('age', 45), help="Patient's age in years")
        gender = st.selectbox("Gender ⚧️", ["Male", "Female"], index=0 if st.session_state.liver_values.get('gender', 'Male') == 'Male' else 1, help="Patient's biological gender")

        st.subheader("Liver Function Tests")
        total_bilirubin = st.number_input("Total Bilirubin (mg/dL) 🟡", 0.1, 100.0, value=st.session_state.liver_values.get('total_bilirubin', 1.0), step=0.1, help="Total bilirubin level in blood (normal: 0.1-1.2 mg/dL)")
        direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL) 🟠", 0.1, 50.0, value=st.session_state.liver_values.get('direct_bilirubin', 0.3), step=0.1, help="Direct bilirubin level (normal: 0.0-0.3 mg/dL)")
        alkaline_phosphotase = st.number_input("Alkaline Phosphotase (IU/L) ⚗️", 10, 2000, value=st.session_state.liver_values.get('alkaline_phosphotase', 200), help="ALP enzyme level (normal: 44-147 IU/L)")
        alamine_aminotransferase = st.number_input("Alamine Aminotransferase (IU/L) 🧪", 1, 2000, value=st.session_state.liver_values.get('alamine_aminotransferase', 30), help="ALT/SGPT enzyme level (normal: 7-56 IU/L)")
        aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase (IU/L) 🔬", 1, 2000, value=st.session_state.liver_values.get('aspartate_aminotransferase', 35), help="AST/SGOT enzyme level (normal: 10-40 IU/L)")
        total_protiens = st.number_input("Total Proteins (g/dL) 🥩", 1.0, 15.0, value=st.session_state.liver_values.get('total_protiens', 7.0), step=0.1, help="Total protein in blood (normal: 6.0-8.3 g/dL)")
        albumin = st.number_input("Albumin (g/dL) 🧬", 0.5, 10.0, value=st.session_state.liver_values.get('albumin', 4.0), step=0.1, help="Albumin protein level (normal: 3.5-5.5 g/dL)")
        ag_ratio = st.number_input("Albumin/Globulin Ratio 📊", 0.1, 5.0, value=st.session_state.liver_values.get('ag_ratio', 1.0), step=0.1, help="A/G ratio (normal: 1.0-2.5)")
        
        if st.button("🔍 Predict Liver Disease", type="primary"):
            # Encode gender
            gender_enc = encode_gender(gender)
            
            # Create feature array
            features = np.array([[age, gender_enc, total_bilirubin, direct_bilirubin, 
                                alkaline_phosphotase, alamine_aminotransferase, 
                                aspartate_aminotransferase, total_protiens, albumin, ag_ratio]])
            
            # Scale and predict
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
            prediction_proba = model.predict_proba(features_scaled)[0]
            
            st.markdown("---")
            st.subheader("📊 Prediction Result")
            
            confidence = prediction_proba[prediction]*100
            
            # Display confidence gauge and result
            col_gauge, col_result = st.columns([1, 1])
            
            with col_gauge:
                fig = create_confidence_gauge(confidence, "Prediction Confidence")
                st.plotly_chart(fig, use_container_width=True)
            
            with col_result:
                if prediction == 1:  # Liver Disease
                    st.markdown(f'<div class="gradient-card"><h2>⚠️ Liver Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                    st.warning("⚠️ **Recommendation:** Consult a hepatologist for further evaluation.")
                else:
                    st.markdown(f'<div class="success-box"><h2>✅ No Liver Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                    st.info("💡 **Recommendation:** Maintain a healthy lifestyle and avoid excessive alcohol.")
