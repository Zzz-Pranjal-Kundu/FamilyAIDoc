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
    st.set_page_config(
        page_title="Family AI Medical Assistant",
        layout="centered"
    )
    st.title("🩺 Interactive Health Assistant")
    st.caption("AI-powered triage using a verified medical database (Convex + Groq)")
    st.warning("⚠️ Informational only. Not a substitute for a doctor.")

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