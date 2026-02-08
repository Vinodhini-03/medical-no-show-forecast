"""
Medical Appointment Management System
Professional Healthcare UI - Streamlit Native
"""

import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Medical Appointment AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (simplified)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: #f8f9fa;
    }
    
    .main .block-container {
        padding-top: 2rem;
        max-width: 1400px;
    }
    
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #0a4d68 0%, #088395 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #088395 0%, #0a4d68 100%);
        box-shadow: 0 4px 12px rgba(8, 131, 149, 0.3);
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #088395;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🏥 Medical Appointment AI System")
st.markdown("### *Advanced Machine Learning for Healthcare Optimization & Patient Care*")
st.divider()

# Feature Cards using Streamlit columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🎯 No-Show Risk Predictor")
    st.markdown("""
    Identify patients at risk of missing appointments using advanced machine learning. 
    Our AI model analyzes patient demographics, historical patterns, weather conditions, 
    and appointment details to predict no-show probability with high accuracy.
    """)
    
    # Metrics in expander for clean look
    with st.expander("📊 Model Performance Metrics", expanded=True):
        m1, m2 = st.columns(2)
        with m1:
            st.metric("F1-Score", "0.7261", "Target: >0.70 ✓")
            st.metric("No-Show Detection", "74%", "+40% vs baseline")
        with m2:
            st.metric("ROC-AUC", "0.8795", "Target: >0.75 ✓")
            st.metric("Est. Savings", "$140K+", "per period")
    
    st.markdown("")
    if st.button("🚀 Launch No-Show Predictor", key="predictor"):
        st.switch_page("pages/1_NoShow_Predictor.py")

with col2:
    st.markdown("### 📈 Demand Forecaster")
    st.markdown("""
    Optimize staffing and resource allocation with AI-powered demand forecasting. 
    Our system predicts daily appointment volumes using temporal patterns, seasonality, 
    and environmental factors to ensure efficient clinic operations.
    """)
    
    with st.expander("📊 Model Performance Metrics", expanded=True):
        m1, m2 = st.columns(2)
        with m1:
            st.metric("R² Score", "0.7534", "Target: >0.65 ✓")
            st.metric("Variance Explained", "75.3%", "High accuracy")
        with m2:
            st.metric("Accuracy", "±80", "appointments/day")
            st.metric("Efficiency Gain", "35%+", "vs manual")
    
    st.markdown("")
    if st.button("🚀 Launch Demand Forecaster", key="forecaster"):
        st.switch_page("pages/2_Demand_Forecaster.py")

st.divider()

# Key Insights
st.markdown("## 💡 Key Insights from Data Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Overall No-Show Rate",
        value="31.8%",
        delta="-5% with interventions",
        delta_color="inverse"
    )
    st.caption("Baseline no-show rate across all appointments")

with col2:
    st.metric(
        label="Top Predictive Factor",
        value="Location",
        help="Geographic patterns strongly influence attendance"
    )
    st.caption("Historical no-show rate by place is key")

with col3:
    st.metric(
        label="Weather Impact",
        value="High",
        help="Rain and temperature significantly affect attendance"
    )
    st.caption("Rain increases no-show likelihood")

st.divider()

# Intervention Strategy
st.markdown("## 🎯 AI-Powered Intervention Strategy")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📋 High-Risk Patient Protocol")
    st.markdown("""
    - **📱 Automated SMS Reminders:** Send targeted messages 48 hours before appointment
    - **📞 Follow-Up Calls:** Contact high-risk patients who haven't confirmed
    - **🌦️ Weather Alerts:** Extra outreach during adverse weather conditions
    - **📍 Location-Based Targeting:** Focused interventions for high no-show areas
    """)

with col2:
    st.markdown("### 📊 Staffing Optimization Strategy")
    st.markdown("""
    - **🔄 Dynamic Scheduling:** AI-driven weekly staffing based on demand forecasts
    - **📈 Peak Management:** Automatic resource allocation during predicted high-volume days
    - **🏥 Multi-Location Coordination:** Optimize staffing across 13 clinic locations
    - **⚡ Backup Management:** Intelligent patient waitlist for unexpected cancellations
    """)

st.divider()

# Footer
st.caption(f"""
🏥 **Medical Appointment AI System** | Random Forest & XGBoost Models | Built with Streamlit  
Last Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
""")