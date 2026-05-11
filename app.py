import textwrap
import streamlit as st
from _pages.chatbox import render_chatbox_page
from config.styles import CUSTOM_CSS
from config.settings import MODEL_INFO, PAGE_CONFIG, PAGES
from components.sidebar import render_sidebar
from _pages.home import render_home
from _pages.kidney import render_kidney_page
from _pages.liver import render_liver_page
from _pages.parkinsons import render_parkinsons_page
from _pages.about_models import render_about_models

# Configure page
st.set_page_config(**PAGE_CONFIG)

# Force clear cache to load newly trained models
st.cache_resource.clear()

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Render sidebar and get selected page
page = render_sidebar()

# Route to selected page
if page == "🏠 Home":
    render_home()
elif page == "🫘 Kidney Disease":
    render_kidney_page()
elif page == "🫀 Liver Disease":
    render_liver_page()
elif page == "🧠 Parkinson's Disease":
    render_parkinsons_page()
elif page == "Medical Chatbot":
    render_chatbox_page()
elif page == "📊 About Models":
    render_about_models()
