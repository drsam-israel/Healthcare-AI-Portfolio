import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Healthcare AI Projects",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR BRANDING
# ---------------------------------------------------

st.sidebar.title("🧠 Dr. Samuel Israel")

st.sidebar.markdown("""

Healthcare AI Portfolio

MIT AI Specialization

Data Scientist | Machine Learning Engineering

Clinical Intelligence | Digital Health Transformation

""")
# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #f4f7fb;
}

.title {
    font-size: 60px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 22px;
    color: #475569;
    line-height: 1.8;
    margin-bottom: 50px;
}

.project-card {

    background: white;

    padding: 40px;

    border-radius: 30px;

    margin-bottom: 35px;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.08);

    border:
    1px solid #e2e8f0;

    transition: all 0.35s ease;

    cursor: pointer;
}

.project-card:hover {

    transform: translateY(-8px);

    box-shadow:
    0 20px 40px rgba(0,0,0,0.15);

    border:
    1px solid #93c5fd;
}
.project-title {

    font-size: 38px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 20px;
}

.project-desc {

    font-size: 21px;

    line-height: 1.95;

    color: #334155;

    margin-bottom: 25px;

    font-weight: 500;
}
            
.metric-box {

    background: #eff6ff;

    padding: 18px;

    border-radius: 20px;

    text-align: center;
}

.metric-number {

    font-size: 30px;

    font-weight: 800;

    color: #1d4ed8;
}

.metric-label {

    font-size: 15px;

    color: #334155;
}

.badge {

    display: inline-block;

    background: #dbeafe;

    color: #1d4ed8;

    padding: 8px 16px;

    border-radius: 20px;

    margin: 5px;

    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div class="title">
Flagship Healthcare AI Platforms
</div>

<div class="subtitle">

A growing portfolio of deployable, executive-level Healthcare AI systems
focused on predictive analytics, operational intelligence, explainable AI,
clinical decision support, and healthcare transformation.

</div>
""", unsafe_allow_html=True)

# =====================================================
# CARDIOINTEL AI
# =====================================================

st.markdown("""
<div class="project-card">

<div class="project-title">
🫀 CardioIntel AI
</div>

<div class="project-desc">

Executive Cardiovascular Intelligence & Explainable Healthcare AI Platform
integrating mortality prediction, biomarker intelligence,
SHAP explainability, readmission prediction,
clinical decision support, and executive healthcare dashboards.

</div>

</div>
""", unsafe_allow_html=True)

st.image(
    "assets/screenshots/cardiointel.png",
    use_container_width=True
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">10K+</div>
    <div class="metric-label">Patient Records</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">18.85%</div>
    <div class="metric-label">Mortality Surveillance</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">AI</div>
    <div class="metric-label">Risk Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">SHAP</div>
    <div class="metric-label">Explainability</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""

<span class="badge">Healthcare AI</span>
<span class="badge">Cardiovascular Analytics</span>
<span class="badge">Mortality Prediction</span>
<span class="badge">Readmission Intelligence</span>
<span class="badge">SHAP Explainability</span>
<span class="badge">Clinical Decision Support</span>

""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View CardioIntel AI",
        "https://cardiointel-ai-8hvwda5isaw3auxwfkznni.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/CardioIntel-AI"
    )
st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# DIAINTEL AI
# =====================================================

st.markdown("""
<div class="project-card">

<div class="project-title">
🩺 DiaIntel AI
</div>

<div class="project-desc">

Enterprise Diabetes Readmission Intelligence Platform
developed for diabetes utilization analytics,
predictive healthcare intelligence,
occupancy forecasting,
readmission prediction,
and executive operational dashboards.

</div>

</div>
""", unsafe_allow_html=True)

st.image(
    "assets/screenshots/diaintel.png",
    use_container_width=True
)
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">AI</div>
    <div class="metric-label">Predictive Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">Ops</div>
    <div class="metric-label">Operational Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">Forecast</div>
    <div class="metric-label">Occupancy Prediction</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">30D</div>
    <div class="metric-label">Readmission Risk</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""

<span class="badge">Diabetes Analytics</span>
<span class="badge">Healthcare Forecasting</span>
<span class="badge">Predictive AI</span>
<span class="badge">Executive Dashboards</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Healthcare Analytics</span>

""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View DiaIntel AI",
        "https://healthcare-executive-intelligence-platform-hhc25m9bn3etmvc6zgx.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/healthcare-executive-intelligence-platform"
    )
st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# HEALTHINTEL AI
# =====================================================

st.markdown("""
<div class="project-card">

<div class="project-title">
🏥 HealthIntel AI
</div>

<div class="project-desc">

Executive Healthcare Operations & Intelligence Platform
focused on healthcare KPI monitoring,
operational visibility,
patient trend intelligence,
strategic analytics,
and healthcare transformation insights.

</div>

</div>
""", unsafe_allow_html=True)

st.image(
    "assets/screenshots/healthintel.png",
    use_container_width=True
)
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">KPI</div>
    <div class="metric-label">Executive Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">BI</div>
    <div class="metric-label">Operational Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">AI</div>
    <div class="metric-label">Healthcare Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">DX</div>
    <div class="metric-label">Digital Transformation</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""

<span class="badge">Healthcare KPIs</span>
<span class="badge">Operational Analytics</span>
<span class="badge">Executive Intelligence</span>
<span class="badge">Healthcare Transformation</span>
<span class="badge">Strategic Dashboards</span>
<span class="badge">Digital Health</span>

""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View HealthIntel AI",
        "https://healthcare-executive-intelligence-ai-platform-ersppv6rafg8uza7.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/Healthcare-Executive-Intelligence-AI-Platform"
    )
st.markdown("<br><br>", unsafe_allow_html=True)

st.success(
    "Premium Healthcare AI project portfolio continuously evolving with deployable executive-level AI systems."
)


# =====================================================
# HEALTHCARE OPERATIONS COMMAND CENTER
# =====================================================

st.markdown("""
<div class="project-card">

<div class="project-title">
🏥 Healthcare Operations Command Center
</div>

<div class="project-desc">

Enterprise Healthcare Operations Intelligence System
designed for real-world hospital workflow analytics,
bed occupancy monitoring,
ICU utilization intelligence,
patient flow analytics,
length-of-stay insights,
operational forecasting,
executive KPI tracking,
and healthcare decision support.

</div>

</div>
""", unsafe_allow_html=True)

st.image(
    "assets/screenshots/executive_command_center.png",
    use_container_width=True
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">LOS</div>
    <div class="metric-label">Length-of-Stay Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">ICU</div>
    <div class="metric-label">ICU Utilization Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">OPS</div>
    <div class="metric-label">Operational Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-box">
    <div class="metric-number">KPI</div>
    <div class="metric-label">Executive Command Center</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""

<span class="badge">Healthcare Operations</span>
<span class="badge">Patient Flow Analytics</span>
<span class="badge">Bed Occupancy Intelligence</span>
<span class="badge">ICU Utilization</span>
<span class="badge">Operational Forecasting</span>
<span class="badge">Executive KPIs</span>

""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View Healthcare Operations Command Center",
        "https://enterprise-healthcare-operations-intelligence-system-kxqd4qjp6.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/enterprise-healthcare-operations-intelligence-system"
    )

st.markdown("<br><br>", unsafe_allow_html=True)

st.success(
    "Enterprise Healthcare Operations Intelligence platform supporting hospital workflow analytics, operational visibility, patient flow intelligence, and executive healthcare decision support."
)