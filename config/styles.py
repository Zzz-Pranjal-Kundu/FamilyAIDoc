"""
Centralized styling configuration for FamilyAIDoc application.
Contains all CSS styles used throughout the app.
"""

CUSTOM_CSS = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --bg-color: #0b051a;
        --card-bg: rgba(35, 15, 55, 0.6);
        --card-border: rgba(255, 0, 128, 0.3);
        --primary-mint: #00f0ff;
        --electric-blue: #ff007f;
        --text-main: #f4ebff;
        --text-muted: #b794f6;
        --glass-bg: rgba(20, 8, 35, 0.8);
        --glass-border: rgba(0, 240, 255, 0.3);
        --accent-kidney: #00f0ff;
        --accent-liver: #ff007f;
        --accent-neuro: #8b5cf6;
        --slate-950: #0b051a;
        --slate-900: #1a0b2e;
        --slate-800: #2d1b4e;
        --glass: rgba(35, 15, 55, 0.6);
    }

    * {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        letter-spacing: -0.5px;
    }

    /* Overall App Background */
    .stApp {
        background-color: var(--bg-color);
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(255, 0, 128, 0.12), transparent 30%),
            radial-gradient(circle at 85% 30%, rgba(0, 240, 255, 0.12), transparent 30%);
        color: var(--text-main);
    }

    /* Headers */
    h1 {
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 3rem !important;
        margin-bottom: 0.5rem !important;
    }

    /* Inputs & Selectboxes Styling */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 12px !important;
        color: white !important;
        transition: all 0.3s ease;
    }

    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="select"] > div:hover {
        border-color: rgba(59, 130, 246, 0.4) !important;
        background-color: rgba(30, 41, 59, 0.8) !important;
    }

    /* Input text color */
    input[type="number"], input[type="text"], div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Labels */
    .stNumberInput label, .stSelectbox label, .stTextInput label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.4rem;
        font-family: 'Outfit', sans-serif !important;
    }

    /* Primary Buttons */
    button[kind="primary"] {
        background: linear-gradient(135deg, #ff007f 0%, #b30059 100%) !important;
        color: white !important;
        border: 1px solid rgba(255, 0, 128, 0.5) !important;
        border-radius: 4px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 0 15px rgba(255, 0, 128, 0.4) !important;
        transition: all 0.2s ease !important;
    }

    button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 25px rgba(255, 0, 128, 0.6), 0 0 10px rgba(0, 240, 255, 0.4) !important;
    }

    /* Secondary Buttons */
    button[kind="secondary"] {
        background: rgba(30, 41, 59, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }

    button[kind="secondary"]:hover {
        background: rgba(51, 65, 85, 0.8) !important;
        border-color: rgba(148, 163, 184, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* Glass Container Utilities */
    .glass-container {
        background: var(--card-bg);
        backdrop-filter: blur(16px);
        border: 1px solid var(--card-border);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }

    /* Success / Error Boxes overrides */
    .success-box, .gradient-card, .info-box {
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        text-align: center;
        animation: fadeInUp 0.6s ease-out;
    }

    .success-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.2) 100%);
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.1);
    }
    .success-box h2 { color: #34d399 !important; }

    .gradient-card {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(185, 28, 28, 0.2) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.1);
    }
    .gradient-card h2 { color: #f87171 !important; }

    .info-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #93c5fd;
    }

    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    @keyframes borderPulse {
        0% { border-color: rgba(239, 68, 68, 0.3); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        50% { border-color: rgba(239, 68, 68, 0.6); box-shadow: 0 0 20px rgba(239, 68, 68, 0.1); }
        100% { border-color: rgba(239, 68, 68, 0.3); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
    }
    @keyframes pulseSync {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.5); opacity: 0.5; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* ----- Home Page Specific ----- */
    .hero-container {
        padding: 5.5rem 2.5rem;
        border-radius: 16px;
        background:
            radial-gradient(circle at 20% 20%, rgba(255,0,128,0.2), transparent 40%),
            radial-gradient(circle at 80% 30%, rgba(0,240,255,0.2), transparent 45%),
            linear-gradient(180deg, #0b051a, #1a0b2e);
        border: 2px solid rgba(0,240,255,0.3);
        text-align: center;
        margin-bottom: 4rem;
        box-shadow:
            0 20px 60px -20px rgba(255,0,128,0.4),
            inset 0 0 20px rgba(0,240,255,0.1);
        animation: fadeInUp 0.9s ease-out;
    }
    .hero-icon {
        font-size: 3.8rem;
        margin-bottom: 1.2rem;
        filter: drop-shadow(0 0 20px rgba(255,0,128,0.6));
    }
    .hero-title {
        font-size: 4.8rem;
        font-weight: 900;
        margin-bottom: 1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        background: linear-gradient(180deg, #00f0ff 0%, #ff007f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255,0,128,0.3);
    }
    .hero-badge {
        display: inline-block;
        padding: 0.45rem 1.2rem;
        border-radius: 999px;
        background: rgba(16,185,129,0.12);
        color: var(--primary-mint);
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1.6rem;
        border: 1px solid rgba(16,185,129,0.25);
    }
    .hero-description {
        color: #94a3b8;
        max-width: 780px;
        margin: 0 auto;
        font-size: 1.1rem;
        line-height: 1.9;
    }
    .hero-description strong {
        color: #e5e7eb;
        font-weight: 600;
    }
    .glass-card {
        background: var(--glass);
        backdrop-filter: blur(12px);
        padding: 2.5rem 2rem;
        border-radius: 24px;
        border: 1px solid var(--glass-border);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .glass-card:hover {
        transform: translateY(-15px) scale(1.02);
        border-color: var(--primary-mint);
        box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6);
        background: rgba(30, 41, 59, 0.75);
    }
    .icon-wrapper {
        animation: float 4s ease-in-out infinite;
    }
    .tech-box-modern {
        background: linear-gradient(165deg, #0a0f1a 0%, #020617 100%);
        padding: 3rem;
        border-radius: 28px;
        border: 1px solid var(--glass-border);
        border-left: 6px solid var(--primary-mint);
        box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);
    }
    .step-card-modern {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2.5rem 1.5rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        animation: fadeInUp 0.8s ease-out;
    }
    .step-card-modern:hover {
        transform: translateY(-12px);
        border-color: #3b82f6;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.4), 0 0 15px rgba(59, 130, 246, 0.2);
        background: #1e293b;
    }
    .step-icon-box {
        width: 60px;
        height: 60px;
        margin: 0 auto 1.5rem auto;
        background: rgba(59, 130, 246, 0.1);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #3b82f6;
    }
    .step-badge {
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #3b82f6;
        margin-bottom: 0.5rem;
        display: block;
    }
    .step-title-modern {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    .step-desc-modern {
        color: #94a3b8;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    .legal-warning-container {
        margin-top: 4rem;
        padding: 2.5rem;
        background: linear-gradient(165deg, rgba(239, 68, 68, 0.08) 0%, rgba(127, 29, 29, 0.15) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 24px;
        backdrop-filter: blur(10px);
        animation: borderPulse 4s infinite;
    }
    .warning-title {
        color: #fca5a5 !important;
        font-size: 1.1rem !important;
        font-weight: 800 !important;
        letter-spacing: 1.5px !important;
        margin: 0 !important;
        text-transform: uppercase;
    }

    /* ----- About Models Specific ----- */
    .model-card {
        position: relative;
        background: var(--glass-bg);
        backdrop-filter: blur(14px);
        border: 1px solid var(--glass-border);
        border-radius: 28px;
        padding: 2.5rem;
        margin-bottom: 3rem;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease-out backwards;
    }
    .pattern-dots::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background-image: radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
        background-size: 24px 24px; pointer-events: none;
    }
    .pattern-waves::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(139, 92, 246, 0.02) 10px, rgba(139, 92, 246, 0.02) 11px);
        pointer-events: none;
    }
    .model-card:hover {
        transform: translateY(-10px);
        border-color: rgba(255,255,255,0.2);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    .card-1 { animation-delay: 0.2s; border-left: 5px solid var(--accent-kidney); }
    .card-2 { animation-delay: 0.4s; border-left: 5px solid var(--accent-liver); }
    .card-3 { animation-delay: 0.6s; border-left: 5px solid var(--accent-neuro); }
    .severity-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 1rem;
        background: rgba(239, 68, 68, 0.1);
        color: #ef4444;
        border: 1px solid rgba(239, 68, 68, 0.2);
    }
    .health-tip-box {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 16px;
        transition: 0.3s;
    }
    .pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 50px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        margin: 4px 2px;
        font-size: 0.8rem;
    }
    .dashboard-container {
        margin-top: 3rem;
        padding: 2.5rem;
        background: linear-gradient(165deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.8) 100%);
        border-radius: 30px;
        border: 1px solid rgba(59, 130, 246, 0.2);
        backdrop-filter: blur(15px);
    }
    .dashboard-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1rem;
    }
    .dashboard-title {
        color: #ffffff !important;
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        letter-spacing: -0.5px;
    }
    .dashboard-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 2.5rem;
        max-width: 600px;
    }
    .pulse-indicator {
        width: 10px;
        height: 10px;
        background: #3b82f6;
        border-radius: 50%;
        box-shadow: 0 0 10px #3b82f6;
        animation: pulseSync 2s infinite;
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 20px;
        margin-bottom: 2rem;
    }
    .metric-item {
        background: rgba(255, 255, 255, 0.03);
        padding: 1.5rem 1rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-item:hover {
        background: rgba(59, 130, 246, 0.05);
        border-color: rgba(59, 130, 246, 0.3);
        transform: translateY(-5px);
    }
    .metric-viz {
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .accuracy-glow { color: #10b981; }
    .precision-glow { color: #3b82f6; }
    .recall-glow { color: #f59e0b; }
    .f1-glow { color: #8b5cf6; }
    .metric-label {
        color: #f8fafc;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 8px;
    }
    .metric-info {
        color: #64748b;
        font-size: 0.75rem;
        line-height: 1.4;
    }
    .advanced-metrics-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    .pill-outline {
        padding: 5px 15px;
        border-radius: 50px;
        border: 1px solid rgba(148, 163, 184, 0.3);
        color: #94a3b8;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ----- Chatbot UI Specific ----- */
    div[data-testid="stChatMessage"] {
        background-color: var(--card-bg);
        padding: 1rem 1.2rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        width: fit-content;
        max-width: 85%;
        display: flex;
        gap: 1rem;
    }
    
    /* User Message (Aligned Right) */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
        margin-left: auto; /* Pushes to the right */
        flex-direction: row-reverse; /* Puts avatar on the right */
        border: 1px solid rgba(0, 240, 255, 0.4);
        background: linear-gradient(135deg, rgba(35, 15, 55, 0.8) 0%, rgba(0, 240, 255, 0.1) 100%);
        border-right: 4px solid var(--primary-mint);
        border-radius: 25px 25px 5px 25px; /* Chat bubble tail on bottom right */
    }
    
    /* Fix avatar spacing for user (since it's reversed) */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) > div:first-child {
        margin-left: 0.5rem;
    }

    /* Assistant Message (Aligned Left) */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
        margin-right: auto; /* Keeps it on the left */
        border: 1px solid rgba(255, 0, 128, 0.4);
        background: linear-gradient(135deg, rgba(35, 15, 55, 0.8) 0%, rgba(255, 0, 128, 0.1) 100%);
        border-left: 4px solid var(--electric-blue);
        border-radius: 25px 25px 25px 5px; /* Chat bubble tail on bottom left */
    }

    /* Message Text Color */
    div[data-testid="stChatMessage"] p {
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.5;
        margin: 0;
    }

    /* Chat Input Area */
    div[data-testid="stChatInput"] {
        background: var(--glass-bg);
        border: 2px solid var(--electric-blue);
        border-radius: 30px; /* More rounded like a chat app */
        box-shadow: 0 0 20px rgba(255, 0, 128, 0.2);
        padding: 0.2rem 1rem;
        margin-bottom: 1rem;
    }
    
    div[data-testid="stChatInput"] textarea {
        color: white !important;
        font-size: 1rem;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
