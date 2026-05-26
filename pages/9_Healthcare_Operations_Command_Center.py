import streamlit as st
from PIL import Image

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Healthcare Operations Command Center",
    layout="wide"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero-title {
    font-size: 55px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 24px;
    color: #475569;
    line-height: 1.8;
    margin-bottom: 35px;
}

.section-title {
    font-size: 38px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 50px;
    margin-bottom: 25px;
}

.section-text {
    font-size: 20px;
    line-height: 1.9;
    color: #334155;
}

.metric-card {
    background: white;
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow:
    0 8px 25px rgba(0,0,0,0.08);

    border: 1px solid #e2e8f0;
}

.metric-number {
    font-size: 42px;
    font-weight: 800;
    color: #2563eb;
}

.metric-label {
    font-size: 18px;
    color: #475569;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HERO SECTION
# ------------------------------------------------

st.markdown("""
<div class="hero-title">
🏥 Enterprise Healthcare Operations Command Center
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-subtitle">

Deployable Executive Healthcare Operations Intelligence Platform developed for
real-world hospital workflow analytics, patient flow intelligence,
bed occupancy monitoring, ICU utilization analytics,
operational forecasting, executive KPI tracking,
and healthcare operational decision support.

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# BUTTONS
# ------------------------------------------------

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View Live Platform",
        "https://enterprise-healthcare-operations-intelligence-system-kxqd4qjp6.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "YOUR_GITHUB_LINK"
    )

# ------------------------------------------------
# EXECUTIVE METRICS
# ------------------------------------------------

st.markdown("""
<div class="section-title">
Executive Operational Intelligence
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">50K+</div>
        <div class="metric-label">Hospital Records</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">24/7</div>
        <div class="metric-label">Operational Visibility</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">AI</div>
        <div class="metric-label">Operational Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">Real-Time</div>
        <div class="metric-label">Executive Insights</div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------
# BUSINESS PROBLEM
# ------------------------------------------------

st.markdown("""
<div class="section-title">
Healthcare Operations Challenge
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-text">

Healthcare organizations continue to face increasing operational pressure related to:

• ICU congestion  
• bed occupancy strain  
• prolonged patient length of stay  
• inefficient patient flow  
• emergency department overcrowding  
• delayed discharge coordination  
• fragmented operational visibility  
• rising operational costs  

Traditional healthcare reporting systems often lack predictive operational intelligence,
real-time executive visibility, and integrated workflow analytics required for strategic healthcare operations management.

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# PLATFORM CAPABILITIES
# ------------------------------------------------

st.markdown("""
<div class="section-title">
Platform Capabilities
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-text">

✅ Executive Healthcare Operations Dashboard  
✅ ICU Utilization Intelligence  
✅ Bed Occupancy Analytics  
✅ Patient Flow Intelligence  
✅ Length-of-Stay (LOS) Analytics  
✅ Emergency Department Congestion Monitoring  
✅ Operational Forecasting  
✅ Healthcare KPI Monitoring  
✅ Resource Utilization Intelligence  
✅ Executive Decision Support Analytics  

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SCREENSHOT
# ------------------------------------------------

st.markdown("""
<div class="section-title">
Executive Operations Dashboard
</div>
""", unsafe_allow_html=True)

st.image(
    "assets/screenshots/command_center.png",
    use_container_width=True
)

# ------------------------------------------------
# ARCHITECTURE
# ------------------------------------------------

st.markdown("""
<div class="section-title">
Technology Stack
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-text">

• Python  
• Streamlit  
• Pandas  
• Plotly  
• Healthcare Operations Analytics  
• Predictive Operational Intelligence  
• Synthetic MIMIC-IV Inspired Dataset  
• Executive Dashboard Architecture  

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("---")

st.markdown("""
<center>

Built by <b>Dr. Samuel Israel</b><br>
Healthcare AI Specialist | Digital Health Transformation | Healthcare Operations Intelligence

</center>
""", unsafe_allow_html=True)