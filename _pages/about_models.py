import streamlit as st

def render_about_models():
    # ---------- ADVANCED STYLING & ANIMATIONS ----------
    # Using global CSS from config.styles

    # ---------- PAGE HEADER ----------
    st.markdown("""
    <div class="about-header">
        <h1 style="font-weight: 800; letter-spacing: -1px; margin-bottom: 0.5rem;">📊 Model Intelligence</h1>
        <p style='color:#94a3b8; font-size:1.1rem; max-width:800px; line-height:1.6;'>
            Exploring the clinical logic behind FamilyAIDoc. This section details the datasets, 
            biomarkers, and AI architectures used to screen for high-risk chronic conditions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- KIDNEY MODEL ----------

    st.markdown("""
    <div class="model-card card-1 pattern-dots">
        <div class="severity-badge">High Clinical Severity</div>
        <div class="model-title">🫘 Chronic Kidney Disease Model</div>
        <div class="model-section">
            <p style="color:#e2e8f0; font-style: italic; margin-bottom: 1.5rem;">
                <b>Clinical Context:</b> CKD is a "silent killer" that often shows no symptoms until the kidneys are 
                critically damaged. Early detection is vital to prevent total renal failure and the need for dialysis.
            </p>
            <b>Dataset:</b> 400 patients with 24 clinical attributes<br><br>
            <b>Features Used:</b><br>
            • Age, Blood Pressure, Specific Gravity<br>
            • Albumin, Sugar, Red Blood Cells<br>
            • Blood Glucose, Blood Urea, Serum Creatinine<br>
            • Sodium, Potassium, Hemoglobin<br>
            • And 12 more clinical parameters<br><br>
            <b>Algorithms Compared:</b><br>
            <span class="pill">Logistic Regression</span> <span class="pill">KNN</span> 
            <span class="pill">SVC</span> <span class="pill">Decision Tree</span> 
            <span class="pill">Random Forest</span> <span class="pill">XGBoost</span> 
            <span class="pill">Extra Trees</span> <span class="pill">AdaBoost</span> 
            <span class="pill">Neural Network</span><br><br>
            <b>Best Model:</b> <span style="color:#10b981; font-weight:800;">Extra Trees Classifier (100% Training Accuracy)</span>
        </div>
        <div class="health-tip-box" style="background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.15); border-left: 4px solid #10b981;">
            <h4 style="color:#10b981; margin:0 0 0.8rem 0; font-weight:800; text-transform:uppercase; letter-spacing:1px;">🩺 Health Insights & Prevention Tips</h4>
            • Maintain controlled blood pressure and blood sugar levels<br>
            • Stay hydrated but avoid excessive salt intake<br>
            • Get regular kidney function tests if diabetic or hypertensive<br>
            • Avoid unnecessary painkillers and self-medication
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- LIVER MODEL ----------

    st.markdown("""
    <div class="model-card card-2 pattern-dots">
        <div class="severity-badge">Critical Metabolic Risk</div>
        <div class="model-title">🫀 Liver Disease Model</div>
        <div class="model-section">
            <p style="color:#e2e8f0; font-style: italic; margin-bottom: 1.5rem;">
                <b>Clinical Context:</b> The liver performs over 500 vital functions. Chronic liver disease can progress 
                to cirrhosis or liver cancer if metabolic imbalances and inflammatory markers are ignored.
            </p>
            <b>Dataset:</b> 583 patients (416 liver patients, 167 non-liver patients)<br><br>
            <b>Features Used:</b><br>
            • Age, Gender<br>
            • Total Bilirubin, Direct Bilirubin<br>
            • Alkaline Phosphatase, Alamine Aminotransferase<br>
            • Aspartate Aminotransferase, Total Proteins<br>
            • Albumin, Albumin/Globulin Ratio<br><br>
            <b>Method:</b> <span style="color:#3b82f6; font-weight:700;">PyCaret AutoML</span><br><br>
            <b>Preprocessing Pipeline:</b><br>
            <span class="pill">Missing value imputation</span> 
            <span class="pill">Feature scaling</span> 
            <span class="pill">Categorical encoding</span>
        </div>
        <div class="health-tip-box" style="background: rgba(59,130,246,0.05); border: 1px solid rgba(59,130,246,0.15); border-left: 4px solid #3b82f6;">
            <h4 style="color:#3b82f6; margin:0 0 0.8rem 0; font-weight:800; text-transform:uppercase; letter-spacing:1px;">🍃 Health Insights & Prevention Tips</h4>
            • Limit alcohol consumption or avoid it completely<br>
            • Maintain a healthy weight and balanced diet<br>
            • Avoid unnecessary medications and supplements<br>
            • Get vaccinated for Hepatitis B if at risk
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- PARKINSON'S MODEL ----------

    st.markdown("""
    <div class="model-card card-3 pattern-waves">
        <div class="severity-badge">Degenerative Neurological Concern</div>
        <div class="model-title">🧠 Parkinson's Disease Model</div>
        <div class="model-section">
            <p style="color:#e2e8f0; font-style: italic; margin-bottom: 1.5rem;">
                <b>Clinical Context:</b> Parkinson's is a progressive disorder of the central nervous system. 
                Early vocal biomarkers (dysphonia) often appear before physical tremors, making AI-based voice 
                analysis a breakthrough in early diagnosis.
            </p>
            <b>Dataset:</b> 195 voice recordings (147 with PD, 48 healthy)<br><br>
            <b>Features Used:</b><br>
            • 24 voice measurement features<br>
            • Jitter, Shimmer variations<br>
            • Noise-to-Harmonics Ratio<br>
            • Fundamental frequency measures<br>
            • And more vocal biomarkers<br><br>
            <b>Algorithm:</b> <span style="color:#8b5cf6; font-weight:700;">XGBoost (eXtreme Gradient Boosting)</span><br><br>
            <b>Key Advantages:</b><br>
            • Excellent performance on tabular data<br>
            • Handles complex patterns & regularization<br>
            • Fast training and inference speed
        </div>
        <div class="health-tip-box" style="background: rgba(139,92,246,0.05); border: 1px solid rgba(139,92,246,0.15); border-left: 4px solid #8b5cf6;">
            <h4 style="color:#8b5cf6; margin:0 0 0.8rem 0; font-weight:800; text-transform:uppercase; letter-spacing:1px;">🧠 Health Insights & Lifestyle Tips</h4>
            • Engage in regular physical and speech exercises<br>
            • Early neurological screening improves management<br>
            • Maintain social interaction and mental stimulation<br>
            • Follow a balanced diet rich in antioxidants
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- METRICS ----------
    st.markdown("""
    <div class="dashboard-container">
        <div class="dashboard-header">
            <div class="pulse-indicator"></div>
            <h3 class="dashboard-title">Quality Assurance & Clinical Evaluation</h3>
        </div>
        <p class="dashboard-subtitle">
            To ensure diagnostic integrity, every FamilyAIDoc model undergoes rigorous validation against 
            standardized medical AI benchmarks.
        </p>
        <div class="metrics-grid">
            <div class="metric-item">
                <div class="metric-viz accuracy-glow">92%+</div>
                <div class="metric-label">Accuracy</div>
                <div class="metric-info">Overall correctness of the model across all classes.</div>
            </div>
            <div class="metric-item">
                <div class="metric-viz precision-glow">High</div>
                <div class="metric-label">Precision</div>
                <div class="metric-info">Reliability of positive predictions (minimizing false alarms).</div>
            </div>
            <div class="metric-item">
                <div class="metric-viz recall-glow">Critical</div>
                <div class="metric-label">Recall</div>
                <div class="metric-info">Ability to find all positive cases (minimizing missed diagnoses).</div>
            </div>
            <div class="metric-item">
                <div class="metric-viz f1-glow">Balanced</div>
                <div class="metric-label">F1-Score</div>
                <div class="metric-info">The harmonic mean of precision and recall for robust evaluation.</div>
            </div>
        </div>
        <div class="advanced-metrics-bar">
            <span class="pill-outline">ROC-AUC Curve</span>
            <span class="pill-outline">Confusion Matrix Analysis</span>
            <span class="pill-outline">Cross-Validation (k=10)</span>
        </div>
        <br>
        <div class="metrics-box">
            <div style="font-size:1.2rem; font-weight:800; margin-bottom:1rem; display:flex; align-items:center; gap:10px;">
                📈 Quality Assurance & Evaluation
            </div>
            All models are strictly evaluated using standard medical AI metrics:<br>
            <span class="pill">Accuracy</span> <span class="pill">Precision</span> 
            <span class="pill">Recall</span> <span class="pill">F1-Score</span> 
            <span class="pill">ROC-AUC Score</span> <span class="pill">Confusion Matrix</span>
        </div>
    </div>
    """, unsafe_allow_html=True)