import streamlit as st
import textwrap

def render_home():

    # Using global CSS from config.styles

    # ---------- HERO SECTION ----------
    st.markdown("""
    <div class="hero-container">
        <div style="font-size: 3.5rem; margin-bottom: 1rem;">🏥</div>
        <h1>FamilyAIDoc</h1>
        <p style="color: var(--primary-mint); font-weight: 700; font-size: 1.1rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 1.5rem;">
            Advanced Bio-Informatics & Early Detection
        </p>
        <p style="color: #94a3b8; max-width: 750px; margin: 0 auto; line-height: 1.8; font-size: 1.1rem;">
            Bridging the gap between raw clinical data and life-saving insights. FamilyAIDoc employs 
            ensemble learning architectures to provide fast, explainable, and highly accurate screenings 
            for chronic health conditions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- DISEASE MODULES ----------
    st.markdown('<h2 style="color:white; margin: 3rem 0 2rem 0; font-weight: 800; letter-spacing: -1px;">🎯 Precision Diagnostic Modules</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Re-usable Icon Logic
    kidney_svg = '<svg class="icon-wrapper" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
    liver_svg = '<svg class="icon-wrapper" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16 12-4-4-4 4M12 16V8"/></svg>'
    neuro_svg = '<svg class="icon-wrapper" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1 .34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 3.8-2.54Z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0-.34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-3.8-2.54Z"/></svg>'

    with col1:
        st.markdown(f"""
        <div class="glass-card">
            <div style="margin-bottom: 1.5rem;">{kidney_svg}</div>
            <h3 style="color:white; font-size: 1.5rem; margin-bottom: 1rem;">Kidney Analysis</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.5rem;">
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">Random Forest</span>
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">98.2% ACC</span>
            </div>
            <p style="color:#94a3b8; font-size:0.95rem; line-height: 1.6; flex-grow: 1;">
                Comprehensive screening for Chronic Kidney Disease (CKD) using biochemical markers including Specific Gravity, Albumin, and Hemoglobin levels.
            </p>
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--glass-border); color: var(--primary-mint); font-weight: 800; font-size: 0.75rem; letter-spacing: 1px;">
                24 PARAMETER ANALYSIS
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="glass-card">
            <div style="margin-bottom: 1.5rem;">{liver_svg}</div>
            <h3 style="color:white; font-size: 1.5rem; margin-bottom: 1rem;">Liver Screening</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.5rem;">
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">XGBoost</span>
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">94.5% ACC</span>
            </div>
            <p style="color:#94a3b8; font-size:0.95rem; line-height: 1.6; flex-grow: 1;">
                Predictive modeling for hepatic disorders utilizing Liver Function Tests (LFTs), Bilirubin ratios, and SGOT/SGPT enzyme distributions.
            </p>
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--glass-border); color: var(--primary-mint); font-weight: 800; font-size: 0.75rem; letter-spacing: 1px;">
                10 PARAMETER ANALYSIS
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="glass-card">
            <div style="margin-bottom: 1.5rem;">{neuro_svg}</div>
            <h3 style="color:white; font-size: 1.5rem; margin-bottom: 1rem;">Parkinson's</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.5rem;">
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">Ensemble SVM</span>
                <span class="custom-tag" style="background: rgba(16, 185, 129, 0.1); color: #10b981; border-color: rgba(16, 185, 129, 0.2);">92.1% ACC</span>
            </div>
            <p style="color:#94a3b8; font-size:0.95rem; line-height: 1.6; flex-grow: 1;">
                Early neuro-degenerative detection via multi-dimensional vocal biomarker analysis including MDVP Jitter, Shimmer, and HNR ratios.
            </p>
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--glass-border); color: var(--primary-mint); font-weight: 800; font-size: 0.75rem; letter-spacing: 1px;">
                22 VOICE BIOMARKERS
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- HOW IT WORKS ----------
    st.write("---")
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 2rem;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2"><path d="M10 2v7.5M14 2v7.5M6 12v5a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-5M12 12v5"/></svg>
            <h2 style="color: white; margin: 0;">How FamilyAIDoc Works</h2>
        </div>
    """, unsafe_allow_html=True)

    # 3. INTERACTIVE CARDS
    s1, s2, s3, s4 = st.columns(4)

    # SVG Icons for each step
    icons = {
        "data": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12V7a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h7"/><path d="M16 19h6"/><path d="M19 16v6"/><path d="M7 10h10"/><path d="M7 14h5"/></svg>',
        "process": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4"/><path d="m4.93 4.93 2.83 2.83"/><path d="M2 12h4"/><path d="m4.93 19.07 2.83-2.83"/><path d="M12 18v4"/><path d="m19.07 19.07-2.83-2.83"/><path d="M18 12h4"/><path d="m19.07 4.93-2.83 2.83"/></svg>',
        "ai": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.5V12h7.5"/><path d="M12 12 5.6 18.4"/><path d="M12 12 18.4 5.6"/><path d="M4.5 12H12v7.5"/></svg>',
        "predict": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>'
    }

    with s1:
        st.markdown(f"""
        <div class="step-card-modern">
            <span class="step-badge">Phase 01</span>
            <div class="step-icon-box">{icons['data']}</div>
            <div class="step-title-modern">Data Acquisition</div>
            <p class="step-desc-modern">Enter precise clinical markers or diagnostic values from lab reports into our secure portal.</p>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown(f"""
        <div class="step-card-modern">
            <span class="step-badge">Phase 02</span>
            <div class="step-icon-box">{icons['process']}</div>
            <div class="step-title-modern">Preprocessing</div>
            <p class="step-desc-modern">The system standardizes data through normalization and handles missing values for accuracy.</p>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown(f"""
        <div class="step-card-modern">
            <span class="step-badge">Phase 03</span>
            <div class="step-icon-box">{icons['ai']}</div>
            <div class="step-title-modern">Neural Inference</div>
            <p class="step-desc-modern">Advanced ML models analyze complex correlations between your biological features.</p>
        </div>
        """, unsafe_allow_html=True)

    with s4:
        st.markdown(f"""
        <div class="step-card-modern">
            <span class="step-badge">Phase 04</span>
            <div class="step-icon-box">{icons['predict']}</div>
            <div class="step-title-modern">Diagnostic Insights</div>
            <p class="step-desc-modern">Receive a detailed probability score and risk assessment generated in real-time.</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------- TECH STACK ----------
    st.write("---")
    st.markdown('<h2 style="color:white; margin: 3rem 0 2rem 0; font-weight: 800;">💻 Core Infrastructure</h2>', unsafe_allow_html=True)
    
    
    
    st.markdown("""
    <div class="tech-box-modern">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem;">
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem;">
                    <div style="width: 8px; height: 24px; background: var(--primary-mint); border-radius: 4px;"></div>
                    <h4 style="color:white; margin:0; font-size: 1.2rem;">Machine Learning</h4>
                </div>
                <ul style="color:#cbd5e1; font-size: 0.95rem; line-height: 2.2; list-style: none; padding: 0;">
                    <li>▹ <b>Scikit-learn:</b> Core Classifier Architectures</li>
                    <li>▹ <b>XGBoost:</b> Optimized Gradient Boosting</li>
                    <li>▹ <b>PyCaret:</b> Automated Pipeline Engineering</li>
                    <li>▹ <b>TensorFlow:</b> Deep Feature Extraction</li>
                </ul>
            </div>
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem;">
                    <div style="width: 8px; height: 24px; background: var(--electric-blue); border-radius: 4px;"></div>
                    <h4 style="color:white; margin:0; font-size: 1.2rem;">System & Visualization</h4>
                </div>
                <ul style="color:#cbd5e1; font-size: 0.95rem; line-height: 2.2; list-style: none; padding: 0;">
                    <li>▹ <b>Streamlit:</b> Reactive Application Framework</li>
                    <li>▹ <b>Plotly:</b> Interactive Diagnostic Charts</li>
                    <li>▹ <b>Pandas:</b> High-Performance Data Handling</li>
                    <li>▹ <b>SciPy:</b> Advanced Signal Processing</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- DISCLAIMER ----------
    st.markdown(
        textwrap.dedent("""
        <div class="legal-warning-container">
            <h3 class="warning-title">
                ⚠ Critical Medical Disclaimer & Limitation of Liability
            </h3>
            <p style="color:#ffffff;font-size:1.05rem;">
                <strong>FamilyAIDoc is an AI decision-support tool, not a diagnostic device.</strong>
            </p>
            <p style="color:#cbd5e1;line-height:1.6;">
                All predictions are probabilistic outputs generated from machine learning models
                and are intended solely for educational and research purposes.
            </p>
            <ul style="color:#e5e7eb;">
                <li><strong>Physician Oversight:</strong> Interpret results with certified professionals.</li>
                <li><strong>Emergency Use:</strong> Not for urgent medical decisions.</li>
                <li><strong>Clinical Authority:</strong> Does not replace lab tests or exams.</li>
            </ul>
            <p style="font-size:0.8rem;color:#94a3b8;">
                Use of this platform implies acceptance of these limitations.
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )