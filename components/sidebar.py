"""
Sidebar navigation component for FamilyAIDoc.
"""

import streamlit as st
from config.settings import PAGES


# def render_sidebar():
#     """
#     Render the sidebar navigation and information.
    
#     Returns:
#         str: Selected page from navigation
#     """
#     st.sidebar.title("🏥 FamilyAIDoc")
#     st.sidebar.markdown("---")
    
#     # Navigation menu
#     page = st.sidebar.radio(
#         "Navigate to:",
#         PAGES
#     )
    
#     st.sidebar.markdown("---")
#     st.sidebar.info(
#         "**FamilyAIDoc** uses advanced machine learning algorithms "
#         "to predict the likelihood of chronic diseases based on clinical parameters."
#     )
    
#     # Footer
#     st.sidebar.markdown("---")
#     st.sidebar.markdown("**Developed for Educational Purposes**")
#     st.sidebar.markdown("© 2025 FamilyAIDoc")
    
#     return page



def render_sidebar():
    st.sidebar.empty()

    # ---------- SIDEBAR THEME ----------
    st.markdown("""
    <style>
    /* Sidebar shell */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b0f14 0%, #020617 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    section[data-testid="stSidebar"] > div {
        padding: 1.6rem 1.2rem 2rem 1.2rem;
    }

    /* Brand */
    .sidebar-brand h2 {
        margin: 0;
        font-size: 1.45rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #f9fafb;
    }

    .sidebar-tagline {
        font-size: 0.7rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 1.8rem;
    }
    
    /* Brand container */
    .sidebar-brand-wrap {
        padding-bottom: 1.4rem;
        margin-bottom: 1.6rem;
        border-bottom: 1px solid rgba(255,255,255,0.06);
    }

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .sidebar-logo {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: linear-gradient(145deg, #14b8a6, #0ea5a5);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.25);
    }

    .sidebar-brand h2 {
        margin: 0;
        font-size: 1.45rem;
        font-weight: 800;
        letter-spacing: -0.4px;
        color: #f9fafb;
        line-height: 1.1;
    }

    .sidebar-tagline {
        margin-left: 48px;
        margin-top: 0.3rem;
        font-size: 0.65rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #9ca3af;
    }

    /* Section label */
    .sidebar-section {
        font-size: 0.65rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #6b7280;
        margin-bottom: 0.6rem;
    }

    /* Radio container */
    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 6px;
    }

    /* Radio option */
    div[data-testid="stRadio"] div[role="radiogroup"] label {
        position: relative;
        background: rgba(255,255,255,0.025);
        border-radius: 10px;
        padding: 0.55rem 0.75rem 0.55rem 0.85rem;
        border: 1px solid rgba(255,255,255,0.05);
        transition: all 0.2s ease;
        font-size: 0.9rem;
        color: #e5e7eb;
    }

    /* Hover */
    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background: rgba(20,184,166,0.08);
        border-color: rgba(20,184,166,0.25);
    }

    /* ACTIVE PAGE */
    div[data-testid="stRadio"] input:checked + div {
        background: rgba(20,184,166,0.14);
        border-color: rgba(20,184,166,0.6);
        color: #ecfeff;
    }

    /* Left accent bar for active item */
    div[data-testid="stRadio"] input:checked + div::before {
        content: "";
        position: absolute;
        left: 0;
        top: 6px;
        bottom: 6px;
        width: 3px;
        border-radius: 3px;
        background: #14b8a6;
    }

    /* Info box */
    div[data-testid="stAlert"] {
        background: rgba(255,255,255,0.035);
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.06);
        color: #d1d5db;
        font-size: 0.85rem;
        line-height: 1.6;
    }

    /* Footer */
    .sidebar-footer {
        margin-top: 3rem;
        padding-top: 1.4rem;
        border-top: 1px solid rgba(255,255,255,0.06);
        text-align: center;
    }

    .footer-section {
        margin-bottom: 0.45rem;
        font-size: 0.72rem;
    }

    .footer-muted {
        color: #9ca3af;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .footer-strong {
        color: #e5e7eb;
        font-weight: 600;
    }

    .footer-brand {
        color: #14b8a6;
        font-weight: 700;
    }

    .footer-made {
        margin-top: 0.8rem;
        color: #cbd5e1;
        font-size: 0.7rem;
    }

    .heart {
        display: inline-block;
        margin: 0 2px;
    }

    .footer-names {
        margin-top: 0.5rem;
        display: flex;
        flex-direction: column;
        gap: 0.35rem;
    }

    .footer-name {
        font-size: 0.68rem;
        color: #94a3b8;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- BRAND ----------
    st.sidebar.markdown("""
    <div class="sidebar-brand-wrap">
        <div class="sidebar-brand">
            <div class="sidebar-logo">🏥</div>
            <h2>FamilyAIDoc</h2>
        </div>
        <div class="sidebar-tagline">AI Clinical Intelligence</div>
    </div>
    """, unsafe_allow_html=True)


    # ---------- NAV ----------
    st.sidebar.markdown(
        '<div class="sidebar-section">Navigate</div>',
        unsafe_allow_html=True
    )

    page = st.sidebar.radio(
        "Navigation",
        PAGES,
        label_visibility="collapsed"
    )

    # ---------- INFO ----------
    st.sidebar.markdown("---")
    st.sidebar.info(
        "FamilyAIDoc supports **early detection of chronic diseases** using "
        "clinically validated machine learning models."
    )

    # ---------- FOOTER ----------

    st.sidebar.markdown(
        """
        <div class="sidebar-footer">
            <div class="footer-section footer-muted">
                ⚖️ <span>Educational Use Only</span>
            </div>
            <div class="footer-section footer-strong">
                © 2026 <span class="footer-brand">FamilyAIDoc</span>
            </div>
            <div class="footer-section footer-made">
                Made with <span class="heart">❤️</span> by
            </div>
            <div class="footer-names">
                <div class="footer-name">👩‍💻 
                    <a href="https://www.linkedin.com/in/pranjal-kundu-48606b2b3/"
                    target="_blank"
                    class="footer-link">
                        Pranjal Kundu
                    </a>
                </div>
                <div class="footer-name">👩‍💻 Kritika Rana</div>
                <div class="footer-name">👩‍💻 Yashika Goyal</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    return page