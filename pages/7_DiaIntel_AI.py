import streamlit as st

st.set_page_config(
    page_title="DiaIntel AI",
    page_icon="🩺",
    layout="wide"
)

st.sidebar.title("🧠 Dr. Samuel Israel")
st.sidebar.markdown("""
Healthcare AI Portfolio  
MIT AI Specialization  
Clinical AI | Data Science | ML Engineering
""")

st.markdown("""
<style>
.main { background-color: #f4f7fb; }

.hero {
    background: linear-gradient(135deg, #052e16, #166534, #1e3a8a);
    padding: 55px;
    border-radius: 35px;
    color: white;
    margin-bottom: 40px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.22);
}

.hero h1 {
    font-size: 58px;
    font-weight: 900;
}

.hero p {
    font-size: 22px;
    line-height: 1.8;
}

.card {
    background: white;
    padding: 35px;
    border-radius: 28px;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    transition: all 0.35s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    border: 1px solid #93c5fd;
}

.metric {
    background: #ecfdf5;
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #bbf7d0;
}

.metric h2 {
    color: #15803d;
    font-size: 34px;
    font-weight: 900;
}

.metric p {
    color: #475569;
    font-size: 16px;
}

.badge {
    display: inline-block;
    background: #dcfce7;
    color: #166534;
    padding: 8px 16px;
    border-radius: 22px;
    margin: 5px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🩺 DiaIntel AI</h1>
<p>
Enterprise Diabetes Readmission Intelligence & Predictive Healthcare AI Platform
designed for diabetes utilization analytics, operational intelligence,
occupancy forecasting, readmission prediction, and executive healthcare visibility.
</p>
</div>
""", unsafe_allow_html=True)

st.image("assets/screenshots/diaintel.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown('<div class="metric"><h2>30D</h2><p>Readmission Intelligence</p></div>', unsafe_allow_html=True)

with m2:
    st.markdown('<div class="metric"><h2>AI</h2><p>Predictive Analytics</p></div>', unsafe_allow_html=True)

with m3:
    st.markdown('<div class="metric"><h2>Ops</h2><p>Operational Intelligence</p></div>', unsafe_allow_html=True)

with m4:
    st.markdown('<div class="metric"><h2>Forecast</h2><p>Occupancy Prediction</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Business Challenge</h2>
<p>
Healthcare systems continue to experience increasing diabetes utilization burden,
readmission risk, operational strain, and fragmented operational intelligence.
Traditional reporting systems often lack predictive healthcare visibility and proactive analytics.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>AI Solution</h2>
<p>
DiaIntel AI was developed as an enterprise Healthcare AI platform integrating:
predictive analytics,
occupancy forecasting,
readmission intelligence,
executive dashboards,
operational healthcare visibility,
and strategic healthcare analytics.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Core Capabilities</h2>
<p>
• Diabetes utilization analytics<br>
• Readmission risk prediction<br>
• Occupancy forecasting<br>
• Executive KPI dashboards<br>
• Operational healthcare intelligence<br>
• Strategic healthcare analytics<br>
• Predictive operational visibility
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Technology Stack</h2>
<span class="badge">Python</span>
<span class="badge">Streamlit</span>
<span class="badge">Machine Learning</span>
<span class="badge">Predictive Analytics</span>
<span class="badge">Healthcare Forecasting</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Executive Dashboards</span>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View Live Project",
        "https://healthcare-executive-intelligence-platform-hhc25m9bn3etmvc6zgx.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/healthcare-executive-intelligence-platform"
    )

st.success(
    "DiaIntel AI demonstrates deployable predictive Healthcare AI systems supporting diabetes operational intelligence and executive healthcare analytics."
)