"""
Parkinson's Disease Prediction page.
"""

import streamlit as st
import pandas as pd
import numpy as np
from components.gauges import create_confidence_gauge
from models_utils.model_loader import load_parkinsons_models
from models_utils.sample_data import PARKINSONS_DISEASE_SAMPLE, PARKINSONS_HEALTHY_SAMPLE
from config.settings import PARKINSONS_FEATURES


def render_parkinsons_page():
    """Render the Parkinson's disease prediction page."""
    st.title("🧠 Parkinson's Disease Detection")
    st.markdown("Enter voice measurement features to detect Parkinson's Disease")
    
    # Load model
    model, scaler, features_list = load_parkinsons_models()
    
    if model is None or scaler is None:
        st.error("⚠️ Model not found! Please train the model first by running `python training_scripts/train_parkinsons_xgboost.py`")
    else:
        st.markdown('<div class="info-box">✅ Model loaded successfully - Ready for prediction!</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.info("📝 **Note:** This model uses 22 voice measurement features. You can either enter values manually or upload a CSV file.")
        
        input_method = st.radio("Select Input Method:", ["Manual Entry", "Upload CSV"])
        
        if input_method == "Manual Entry":
            # Sample data buttons
            st.markdown('<span style="font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:0.5em;">🧪 Quick Test Samples</span>', unsafe_allow_html=True)
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
            with col_btn1:
                use_sample_pd = st.button("📊 Load Sample: Parkinson's Patient", use_container_width=True)
            with col_btn2:
                use_sample_healthy = st.button("📊 Load Sample: Healthy Person", use_container_width=True)
            
            # Initialize session state
            if 'parkinsons_values' not in st.session_state:
                st.session_state.parkinsons_values = {}
            
            # Load sample data
            if use_sample_pd:
                st.session_state.parkinsons_values = PARKINSONS_DISEASE_SAMPLE
                st.success("✅ Loaded sample Parkinson's patient voice data")
            
            elif use_sample_healthy:
                st.session_state.parkinsons_values = PARKINSONS_HEALTHY_SAMPLE
                st.success("✅ Loaded sample healthy person voice data")
            
            st.markdown("---")
            
            # Frequency Measures
            st.markdown('<span style="font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:0.5em;">Frequency Measures <span style="font-size:2rem;">🎵</span></span>', unsafe_allow_html=True)
            st.markdown('<span style="font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:0.5em;">Jitter Measures <span style="font-size:2rem;">🪁</span></span>', unsafe_allow_html=True)
            mdvp_fo = st.number_input("Fo 📢", 50.0, 300.0,
                                     value=st.session_state.parkinsons_values.get('mdvp_fo', 150.0),
                                     step=0.1,
                                     help="Average vocal fundamental frequency (normal: 80-260 Hz)")
            mdvp_fhi = st.number_input("Fhi ⬆️", 100.0, 600.0,
                                      value=st.session_state.parkinsons_values.get('mdvp_fhi', 180.0),
                                      step=0.1,
                                      help="Maximum vocal fundamental frequency")
            mdvp_flo = st.number_input("Flo ⬇️", 50.0, 300.0,
                                      value=st.session_state.parkinsons_values.get('mdvp_flo', 100.0),
                                      step=0.1,
                                      help="Minimum vocal fundamental frequency")
            mdvp_jitter_percent = st.number_input("Jitter% 📊", 0.0, 1.0,
                                                 value=st.session_state.parkinsons_values.get('mdvp_jitter_percent', 0.005),
                                                 step=0.001, format="%.5f",
                                                 help="Measure of variation in frequency (lower is better)")
            mdvp_jitter_abs = st.number_input("JitterAbs 🔍", 0.0, 0.001,
                                             value=st.session_state.parkinsons_values.get('mdvp_jitter_abs', 0.00003),
                                             step=0.000001, format="%.8f",
                                             help="Absolute jitter in microseconds")
            mdvp_rap = st.number_input("RAP 📈", 0.0, 0.1,
                                      value=st.session_state.parkinsons_values.get('mdvp_rap', 0.003),
                                      step=0.001, format="%.5f",
                                      help="Relative Amplitude Perturbation")
            mdvp_ppq = st.number_input("PPQ 📉", 0.0, 0.1,
                                      value=st.session_state.parkinsons_values.get('mdvp_ppq', 0.003),
                                      step=0.001, format="%.5f",
                                      help="Five-point Period Perturbation Quotient")
            jitter_ddp = st.number_input("DDP 📐", 0.0, 0.1,
                                        value=st.session_state.parkinsons_values.get('jitter_ddp', 0.008),
                                        step=0.001, format="%.5f",
                                        help="Average absolute difference of differences")
            
            # Shimmer Measures
            st.markdown('<span style="font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:0.5em;">Shimmer Measures <span style="font-size:2rem;">🌊</span></span>', unsafe_allow_html=True)
            mdvp_shimmer = st.number_input("Shimmer 📊", 0.0, 1.0,
                                          value=st.session_state.parkinsons_values.get('mdvp_shimmer', 0.03),
                                          step=0.001, format="%.5f",
                                          help="Measure of variation in amplitude")
            mdvp_shimmer_db = st.number_input("ShimmerdB 🔊", 0.0, 2.0,
                                         value=st.session_state.parkinsons_values.get('mdvp_shimmer_db', 0.3),
                                         step=0.01,
                                         help="Shimmer in decibels")
            shimmer_apq3 = st.number_input("APQ3 3️⃣", 0.0, 0.1,
                                          value=st.session_state.parkinsons_values.get('shimmer_apq3', 0.015),
                                          step=0.001, format="%.5f",
                                          help="Three-point Amplitude Perturbation Quotient")
            shimmer_apq5 = st.number_input("APQ5 5️⃣", 0.0, 0.1,
                                          value=st.session_state.parkinsons_values.get('shimmer_apq5', 0.017),
                                          step=0.001, format="%.5f",
                                          help="Five-point Amplitude Perturbation Quotient")
            mdvp_apq = st.number_input("APQ 📏", 0.0, 0.1,
                                      value=st.session_state.parkinsons_values.get('mdvp_apq', 0.024),
                                      step=0.001, format="%.5f",
                                      help="11-point Amplitude Perturbation Quotient")
            shimmer_dda = st.number_input("DDA 〰️", 0.0, 0.1,
                                         value=st.session_state.parkinsons_values.get('shimmer_dda', 0.045),
                                         step=0.001, format="%.5f",
                                         help="Average absolute difference between amplitudes")
            
            # Other Measures
            st.markdown('<span style="font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:0.5em;">Other Measures <span style="font-size:2rem;">⚡</span></span>', unsafe_allow_html=True)
            nhr = st.number_input("NHR 🔉", 0.0, 1.0,
                                 value=st.session_state.parkinsons_values.get('nhr', 0.025),
                                 step=0.001, format="%.5f",
                                 help="Noise-to-Harmonics Ratio (lower is better)")
            hnr = st.number_input("HNR 🎼", 5.0, 35.0,
                                 value=st.session_state.parkinsons_values.get('hnr', 20.0),
                                 step=0.1,
                                 help="Harmonics-to-Noise Ratio (higher is better)")
            rpde = st.number_input("RPDE 🔄", 0.2, 0.8,
                                  value=st.session_state.parkinsons_values.get('rpde', 0.5),
                                  step=0.01,
                                  help="Recurrence Period Density Entropy")
            dfa = st.number_input("DFA 📈", 0.5, 0.9,
                                 value=st.session_state.parkinsons_values.get('dfa', 0.7),
                                 step=0.01,
                                 help="Detrended Fluctuation Analysis")
            spread1 = st.number_input("Spread1 📊", -8.0, -2.0,
                                     value=st.session_state.parkinsons_values.get('spread1', -5.0),
                                     step=0.1,
                                     help="Nonlinear measure of fundamental frequency variation")
            spread2 = st.number_input("Spread2 📉", 0.0, 0.5,
                                     value=st.session_state.parkinsons_values.get('spread2', 0.2),
                                     step=0.01,
                                     help="Second nonlinear measure of variation")
            d2 = st.number_input("D2 🌀", 1.0, 4.0,
                                value=st.session_state.parkinsons_values.get('d2', 2.5),
                                step=0.1,
                                help="Correlation dimension")
            ppe = st.number_input("PPE 🎯", 0.0, 0.7,
                                 value=st.session_state.parkinsons_values.get('ppe', 0.2),
                                 step=0.01,
                                 help="Pitch Period Entropy")
            
            if st.button("🔍 Detect Parkinson's Disease", type="primary"):
                # Create feature array
                features = np.array([[mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_percent, 
                                    mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp,
                                    mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5,
                                    mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread1, 
                                    spread2, d2, ppe]])
                
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
                    if prediction == 1:  # Parkinson's
                        st.markdown(f'<div class="gradient-card"><h2>⚠️ Parkinson\'s Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                        st.warning("⚠️ **Recommendation:** Consult a neurologist for comprehensive evaluation.")
                    else:
                        st.markdown(f'<div class="success-box"><h2>✅ No Parkinson\'s Disease Detected</h2><p style="font-size:20px;">Confidence: {confidence:.2f}%</p></div>', unsafe_allow_html=True)
                        st.info("💡 **Recommendation:** Continue regular health monitoring.")
        else:
            uploaded_file = st.file_uploader("Upload CSV file with voice features", type=['csv'])
            if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)
                st.write("Preview of uploaded data:")
                st.dataframe(data.head())
                
                if st.button("🔍 Predict from CSV"):
                    st.info("CSV prediction feature coming soon!")
