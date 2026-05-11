"""
Sidebar navigation component for FamilyAIDoc.
"""

import streamlit as st
from config.settings import PAGES
from utils.ui_helpers import get_base64_of_bin_file
import os

def render_sidebar():
    st.sidebar.empty()

    # Get the 3D cross asset
    cross_b64 = get_base64_of_bin_file(os.path.join("assets", "cross.png"))
    cross_img_src = f"data:image/png;base64,{cross_b64}" if cross_b64 else ""

    # ---------- SIDEBAR THEME ----------
    st.markdown(f"""
    <style>
    /* Sidebar shell */
    section[data-testid="stSidebar"] {{
        background: #0b051a !important; /* Deep void */
        border-right: 1px solid rgba(255, 0, 128, 0.15) !important;
    }}

    section[data-testid="stSidebar"] > div {{
        padding: 1.6rem 1.2rem 2rem 1.2rem;
    }}

    /* Brand container */
    .sidebar-brand-wrap {{
        padding-bottom: 1.4rem;
        margin-bottom: 1.6rem;
    }}

    .sidebar-brand {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .sidebar-logo {{
        width: 36px;
        height: 36px;
        border-radius: 8px;
        background: linear-gradient(135deg, #00f0ff, #ff007f);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
    }}

    .sidebar-brand h2 {{
        margin: 0;
        font-size: 1.5rem;
        font-weight: 900;
        color: #ffffff;
        font-family: 'Outfit', sans-serif;
    }}

    .sidebar-tagline {{
        margin-left: 48px;
        margin-top: 0.3rem;
        font-size: 0.65rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #94a3b8;
    }}

    /* Section label */
    .sidebar-section {{
        font-size: 0.7rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #64748b;
        margin-bottom: 0.8rem;
        font-weight: 700;
    }}

    /* Radio container */
    div[data-testid="stRadio"] div[role="radiogroup"] {{
        gap: 8px;
    }}

    /* Radio option */
    div[data-testid="stRadio"] div[role="radiogroup"] label {{
        position: relative;
        background: transparent;
        border-radius: 12px;
        padding: 0.6rem 0.8rem;
        border: 1px solid transparent;
        transition: all 0.3s ease;
        font-size: 0.95rem;
        color: #cbd5e1;
    }}

    /* Hover */
    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {{
        background: rgba(255, 255, 255, 0.05);
    }}

    /* ACTIVE PAGE */
    div[data-testid="stRadio"] input:checked + div {{
        background: rgba(0, 240, 255, 0.08);
        border-color: rgba(0, 240, 255, 0.3);
        color: #00f0ff;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.1);
    }}

    /* AI Badge Hack for Chatbot */
    div[data-testid="stRadio"] div[role="radiogroup"] label:last-child div[data-testid="stMarkdownContainer"] p::after {{
        content: "AI";
        background: linear-gradient(135deg, #00f0ff, #3b82f6);
        color: #0b051a;
        font-size: 0.65rem;
        font-weight: 800;
        padding: 2px 6px;
        border-radius: 6px;
        margin-left: auto;
        float: right;
    }}

    /* Hide standard st.info */
    div[data-testid="stAlert"] {{
        display: none !important;
    }}

    /* Promo Card */
    .promo-card {{
        margin-top: 2rem;
        background: linear-gradient(145deg, rgba(30, 11, 46, 0.8), rgba(11, 5, 26, 0.9));
        border: 1px solid rgba(255, 0, 128, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}

    .promo-header {{
        color: #94a3b8;
        font-size: 0.65rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }}

    .promo-text {{
        color: #f1f5f9;
        font-size: 0.85rem;
        line-height: 1.5;
        max-width: 75%;
    }}

    .promo-icon {{
        position: absolute;
        bottom: -10px;
        right: -10px;
        width: 80px;
        height: 80px;
        filter: drop-shadow(0 0 10px rgba(0, 240, 255, 0.6));
    }}

    /* System Status */
    .system-status {{
        margin-top: 3rem;
    }}
    .status-header {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.65rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #64748b;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }}
    .dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #10b981;
        box-shadow: 0 0 8px #10b981;
    }}
    .status-text {{
        font-size: 0.8rem;
        color: #94a3b8;
    }}
    .version {{
        margin-top: 1.5rem;
        display: flex;
        justify-content: space-between;
        font-size: 0.75rem;
        color: #475569;
    }}

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
        '<div class="sidebar-section">Navigation</div>',
        unsafe_allow_html=True
    )

    page = st.sidebar.radio(
        "Navigation",
        PAGES,
        label_visibility="collapsed"
    )

    # ---------- PROMO CARD ----------
    st.sidebar.markdown(f"""
        <div class="promo-card">
            <div class="promo-header">AI CLINICAL ASSISTANT</div>
            <div class="promo-text">Advanced medical AI support for faster, smarter, and safer clinical decisions.</div>
            <img src="{cross_img_src}" class="promo-icon" />
        </div>
    """, unsafe_allow_html=True)

    # ---------- SYSTEM STATUS ----------
    st.sidebar.markdown("""
        <div class="system-status">
            <div class="status-header"><div class="dot"></div> SYSTEM STATUS</div>
            <div class="status-text">All systems operational</div>
            <div class="version">
                <span>v2.0.0</span>
                <span class="dot" style="width: 6px; height: 6px; opacity: 0.5;"></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    return page