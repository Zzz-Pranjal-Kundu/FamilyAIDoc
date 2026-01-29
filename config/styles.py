"""
Centralized styling configuration for FamilyAIDoc application.
Contains all CSS styles used throughout the app.
"""

CUSTOM_CSS = """
    <style>
    .info-box:empty {
        display: none !important;
    }
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        max-width: 1400px;
        padding: 0 1rem;
    }
    
    /* Make columns stretch to equal height */
    .row-widget.stHorizontal {
        align-items: stretch !important;
    }
    
    .row-widget.stHorizontal > div {
        display: flex !important;
        flex-direction: column !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
        animation: fadeIn 1s ease-in;
    }
    
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        padding-bottom: 1.5rem;
        animation: fadeIn 1.5s ease-in;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid #667eea;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        flex: 1;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .feature-card h3 {
        font-size: 1.15rem;
        margin-bottom: 0.8rem;
        color: #1f1f1f;
        font-weight: 600;
        line-height: 1.3;
    }
    
    .feature-card p {
        color: #333;
        font-size: 0.9rem;
        line-height: 1.5;
        margin: 0.3rem 0;
    }
    
    .gradient-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 1;
        height: 100%;
    }
    
    .gradient-card h3 {
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .gradient-card p {
        font-size: 0.9rem;
        margin: 0;
        line-height: 1.4;
    }
    
    .gradient-card h3 {
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .gradient-card p {
        font-size: 0.95rem;
        margin: 0;
    }
    
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px solid #667eea;
        margin: 1rem 0;
        color: #1a1a1a;
    }
    
    .info-box h2, .info-box h3, .info-box h4 {
        color: #1a1a1a !important;
        font-weight: 600;
    }
    
    .info-box p, .info-box li {
        color: #2d2d2d !important;
        font-weight: 400;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.6);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .success-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .sub-header {
            font-size: 1rem;
        }
        .feature-card h3, .gradient-card h3 {
            font-size: 1rem;
        }
    }
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        animation: fadeIn 0.5s ease-in;
    }
    
    .tooltip {
        background-color: #667eea;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
    }
    </style>
    """
