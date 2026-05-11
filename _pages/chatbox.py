import streamlit as st
import os
import requests
from dotenv import load_dotenv
from groq import Groq

# ===== PDF SUPPORT (ADDED) =====
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from datetime import datetime
import io


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CONVEX_URL = os.getenv("CONVEX_URL")


# CLIENT SETUP
def get_groq_client():
    if "groq_client" not in st.session_state:
        st.session_state.groq_client = Groq(api_key=GROQ_API_KEY)
    return st.session_state.groq_client


# ===== RESET HELPER (ADDED) =====
def reset_conversation():
    # Soft reset: keep chat, reset medical reasoning
    st.session_state.messages.append({
        "role": "system",
        "content": "---- NEW MEDICAL CASE START ----"
    })

    st.session_state.triage_stage = "initial"
    st.session_state.final_report = None


#  CONVEX SEARCH 
def fetch_top_matches(user_text: str):
    """
    Calls Convex HTTP API to retrieve ranked disease matches.
    """
    if not CONVEX_URL:
        return []

    try:
        r = requests.post(
            f"{CONVEX_URL}/api/search_diseases",
            json={"query": user_text},
            timeout=10
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"Convex error: {e}")
        return []


def generate_pdf_report(messages):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("<b>Medical Triage Report</b>", styles["Title"]))
    story.append(Spacer(1, 0.2 * inch))

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %b %Y, %H:%M')}",
            styles["Normal"]
        )
    )
    story.append(Spacer(1, 0.3 * inch))

    # Chat log
    story.append(Paragraph("<b>Conversation Log</b>", styles["Heading2"]))
    story.append(Spacer(1, 0.2 * inch))

    for msg in messages:
        role = "Patient" if msg["role"] == "user" else "Assistant"
        content = msg["content"].replace("\n", "<br/>")

        story.append(
            Paragraph(f"<b>{role}:</b> {content}", styles["Normal"])
        )
        story.append(Spacer(1, 0.15 * inch))

    # Disclaimer
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("<b>Medical Disclaimer</b>", styles["Heading2"]))
    story.append(
        Paragraph(
            "This report is generated for informational and triage purposes only "
            "and is not a substitute for professional medical advice. "
            "Please consult a qualified healthcare provider for diagnosis and treatment.",
            styles["Normal"]
        )
    )

    doc.build(story)
    buffer.seek(0)
    return buffer



# STREAMLIT UI
def render_chatbox_page():
    # ---------- MOCKUP CSS & HERO ----------
    from utils.ui_helpers import get_base64_of_bin_file
    steth_b64 = get_base64_of_bin_file(os.path.join("assets", "stethoscope.png"))
    steth_img_src = f"data:image/png;base64,{steth_b64}" if steth_b64 else ""

    st.markdown(f"""
    <style>
    /* Chatbox Hero Card */
    .mockup-hero {{
        background: linear-gradient(145deg, #180929 0%, #0d0517 100%);
        border: 1px solid rgba(255, 0, 128, 0.2);
        border-radius: 24px;
        padding: 3rem 4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        position: relative;
        overflow: hidden;
    }}
    .hero-content {{
        max-width: 60%;
        z-index: 2;
    }}
    .hero-badge {{
        background: rgba(0, 240, 255, 0.1);
        color: #00f0ff;
        border: 1px solid rgba(0, 240, 255, 0.3);
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 1.5rem;
    }}
    .hero-main-title {{
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        line-height: 1.1 !important;
        margin: 0 0 1rem 0 !important;
        color: white;
        background: none !important;
        -webkit-text-fill-color: initial !important;
        letter-spacing: -1px;
    }}
    .hero-gradient-text {{
        background: linear-gradient(135deg, #00f0ff 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }}
    .hero-warning {{
        background: rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        display: flex;
        gap: 15px;
        align-items: center;
    }}
    .warning-icon {{
        color: #00f0ff;
        font-size: 1.5rem;
    }}
    .hero-warning strong {{
        color: #e2e8f0;
        font-size: 0.95rem;
    }}
    .warning-subtext {{
        color: #64748b;
        font-size: 0.85rem;
    }}
    .hero-3d-img {{
        position: absolute;
        right: -20px;
        top: 50%;
        transform: translateY(-50%);
        width: 380px;
        filter: drop-shadow(0 0 30px rgba(0,240,255,0.3));
        z-index: 1;
    }}

    /* Quick Links Grid */
    .quick-links-title {{
        color: #e2e8f0;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
    }}
    .quick-link-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-bottom: 3rem;
    }}
    .quick-card {{
        background: rgba(30, 11, 46, 0.4);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.2rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    .quick-card:hover {{
        background: rgba(30, 11, 46, 0.8);
        border-color: rgba(0, 240, 255, 0.3);
        transform: translateY(-5px);
    }}
    .qc-header {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 0.8rem;
    }}
    .qc-icon {{ font-size: 1.5rem; }}
    .qc-title {{
        color: white;
        font-weight: 600;
        font-size: 0.95rem;
        flex-grow: 1;
    }}
    .qc-arrow {{
        color: #64748b;
        font-size: 1.2rem;
    }}
    .qc-desc {{
        color: #64748b;
        font-size: 0.8rem;
        line-height: 1.4;
    }}
    </style>

    <div class="mockup-hero">
        <div class="hero-content">
            <span class="hero-badge">AI ASSISTANT</span>
            <h1 class="hero-main-title">Interactive<br/><span class="hero-gradient-text">Health Assistant</span></h1>
            <p class="hero-subtitle">AI-powered triage using a verified medical database (Convex + Groq)</p>
            <div class="hero-warning">
                <span class="warning-icon">ⓘ</span>
                <div>
                    <strong>Informational only. Not a substitute for a doctor.</strong><br/>
                    <span class="warning-subtext">For medical emergencies, contact your healthcare provider.</span>
                </div>
            </div>
        </div>
        <img src="{steth_img_src}" class="hero-3d-img" />
    </div>

    <div class="quick-links-title">Try asking about</div>
    <div class="quick-link-grid">
        <div class="quick-card">
            <div class="qc-header">
                <span class="qc-icon">🫘</span>
                <span class="qc-title">Kidney Health</span>
                <span class="qc-arrow">›</span>
            </div>
            <div class="qc-desc">Learn about symptoms, tests, and treatment options.</div>
        </div>
        <div class="quick-card">
            <div class="qc-header">
                <span class="qc-icon">🫀</span>
                <span class="qc-title">Liver Conditions</span>
                <span class="qc-arrow">›</span>
            </div>
            <div class="qc-desc">Understand liver diseases, causes, and management.</div>
        </div>
        <div class="quick-card">
            <div class="qc-header">
                <span class="qc-icon">🧠</span>
                <span class="qc-title">Parkinson's</span>
                <span class="qc-arrow">›</span>
            </div>
            <div class="qc-desc">Explore symptoms, stages, and care strategies.</div>
        </div>
        <div class="quick-card">
            <div class="qc-header">
                <span class="qc-icon">❤️</span>
                <span class="qc-title">General Health</span>
                <span class="qc-arrow">›</span>
            </div>
            <div class="qc-desc">Ask general health questions and get guidance.</div>
        </div>
    </div>

    <style>
    .disclaimer-card {{
        background: rgba(30, 11, 46, 0.4);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.2rem;
        display: flex;
        gap: 15px;
        align-items: flex-start;
        margin-bottom: 2rem;
    }}
    .disclaimer-icon {{
        font-size: 1.8rem;
        color: #3b82f6;
    }}
    .disclaimer-title {{
        color: white;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.3rem;
    }}
    .disclaimer-text {{
        color: #64748b;
        font-size: 0.85rem;
        line-height: 1.4;
    }}
    </style>
    <div class="disclaimer-card">
        <div class="disclaimer-icon">🛡️</div>
        <div>
            <div class="disclaimer-title">Important Disclaimer</div>
            <div class="disclaimer-text">FamilyAIDoc provides AI-assisted information only and is not a diagnostic device.<br/>Always consult qualified healthcare professionals for medical advice.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- Session State ----------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "triage_stage" not in st.session_state:
        st.session_state.triage_stage = "initial"

    if "final_report" not in st.session_state:
        st.session_state.final_report = None

    # ---------- Render Chat History ----------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Describe your symptoms in detail...")

    if not user_input:
        return

    # ===== CONTEXT RESET DETECTION (ADDED) =====
    reset_phrases = [
        "thank you", "thanks", "thx", "bye",
        "that helps", "ok thanks", "all good"
    ]

    if any(p in user_input.lower() for p in reset_phrases):
        with st.chat_message("assistant"):
            st.markdown(
                "You're welcome 🙂\n\n"
                "If you have a new concern, feel free to ask anytime."
            )
        reset_conversation()
        return

    # ---------- Store User Message ----------
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------- Fetch from Convex ----------
    potential_matches = fetch_top_matches(user_input)

    # ---------- Build DB Context ----------
    if potential_matches:
        db_context = ""
        for i, entry in enumerate(potential_matches, 1):
            db_context += f"""
{i}. **{entry['name']}**
   - Category: {entry['category']}
   - Symptoms: {", ".join(entry['symptoms'])}
   - Description: {entry['description']}
   - Advice: {entry['advice']}
   - Medicines: {", ".join([m['name'] for m in entry['medicines']])}
   - Database Confidence: {entry['score']} symptom overlaps
"""
    else:
        db_context = "No relevant diseases were found in the database."

    # ---------- SYSTEM PROMPT (UNCHANGED) ----------
    SYSTEM_PROMPT = f"""
You are an AI-powered Medical Triage Assistant.

You have TWO knowledge sources:
1. A VERIFIED MEDICAL DATABASE (provided below)
2. Your general medical knowledge (secondary, supportive)

DATABASE RULES:
- The database is your PRIMARY source of truth.
- Prefer database diseases over inferred ones.
- Do NOT invent medicines or treatments.

======== RESPONSE MODE RULES ========

IF CURRENT TRIAGE STAGE IS "initial" OR "followup":

- DO NOT give full disease descriptions.
- DO NOT list medicines in detail.
- DO NOT give long explanations.
- ONLY do the following:
  • List 2–3 MOST LIKELY diseases (names only)
  • Give 1 short reason per disease (1 sentence max)
  • Ask 2–3 targeted follow-up questions
  • Explain briefly why each question matters

IF CURRENT TRIAGE STAGE IS "final":

- FIRST, list the TOP 2–3 MOST PROBABLE diseases in descending order of likelihood.
- THEN select the MOST LIKELY diagnosis
- Provide confidence level
- Give medicines ONLY from database
- Provide home care advice
- ALWAYS include a medical disclaimer

CURRENT TRIAGE STAGE:
{st.session_state.triage_stage}

DATABASE MATCHES:
{db_context}
"""

    # ---------- LLM RESPONSE ----------
    with st.chat_message("assistant"):
        client = get_groq_client()

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages
            ],
            temperature=0.3,
        )

        reply = response.choices[0].message.content
        st.markdown(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

        # ===== STORE FINAL REPORT (ADDED) =====
        if "most likely diagnosis" in reply.lower() or "final diagnosis" in reply.lower():
            st.session_state.final_report = reply
            st.session_state.triage_stage = "final"

        elif st.session_state.triage_stage == "final":
            st.session_state.triage_stage = "post_final"

        else:
            st.session_state.triage_stage = "followup"


    # ===== PDF DOWNLOAD BUTTON (ADDED) =====
    if st.session_state.final_report:
        st.divider()
        st.subheader("📄 Download Diagnosis Report")

        pdf_buffer = generate_pdf_report(st.session_state.messages)
        st.download_button(
            "📄 Download PDF Report",
            data=pdf_buffer,
            file_name="medical_diagnosis_report.pdf",
            mime="application/pdf"
        )
