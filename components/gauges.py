"""
Gauge and visualization components for displaying prediction confidence.
"""

import plotly.graph_objects as go


def create_confidence_gauge(confidence, title="Confidence"):
    """
    Create a confidence gauge chart using Plotly.
    
    Args:
        confidence (float): Confidence percentage (0-100)
        title (str): Title for the gauge
        
    Returns:
        plotly.graph_objects.Figure: Configured gauge figure
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        title={'text': title, 'font': {'size': 24, 'color': '#667eea'}},
        number={'suffix': "%", 'font': {'size': 40}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#667eea"},
            'bar': {'color': "#667eea"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#667eea",
            'steps': [
                {'range': [0, 50], 'color': '#ffebee'},
                {'range': [50, 75], 'color': '#fff9c4'},
                {'range': [75, 100], 'color': '#c8e6c9'}
            ],
            'threshold': {
                'line': {'color': "#764ba2", 'width': 4},
                'thickness': 0.75,
                'value': confidence
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font={'family': "Poppins"}
    )
    
    return fig
