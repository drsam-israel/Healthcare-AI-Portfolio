import streamlit as st
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Dr. Samuel Israel | MIT, AI Specialization",
    page_icon="🧠",
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
# LOAD IMAGE
# -----------------------------

image = Image.open("assets/profile.jpg")
image = image.resize((220, 220))

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #f4f7fb;
}

.hero-container {
    background:
    linear-gradient(
        135deg,
        #06122e 0%,
        #0f1f4b 45%,
        #1d4ed8 100%
    );

    border-radius: 35px;

    padding: 60px;

    margin-top: 10px;
    margin-bottom: 50px;

    box-shadow:
    0 10px 35px rgba(0,0,0,0.18);

    border:
    1px solid rgba(255,255,255,0.08);
}

.hero-title {
    color: white;
    font-size: 70px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 20px;
}

.hero-subtitle {
    color: #dbeafe;
    font-size: 28px;
    line-height: 1.6;
    margin-bottom: 30px;
    font-weight: 600;
}

.hero-text {
    color: #e2e8f0;
    font-size: 22px;
    line-height: 1.9;
}

.metric-card {
    background: white;

    padding: 30px;

    border-radius: 25px;

    text-align: center;

    box-shadow:
    0 5px 20px rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

.metric-number {
    font-size: 40px;
    font-weight: 800;
    color: #1d4ed8;
}

.metric-label {
    font-size: 18px;
    color: #334155;
}

.section-title {
    font-size: 42px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 25px;
    color: #0f172a;
}

.project-card {
    background: white;

    padding: 35px;

    border-radius: 30px;

    box-shadow:
    0 10px 25px rgba(0,0,0,0.08);

    margin-bottom: 30px;

    border:
    1px solid #e2e8f0;
}

.project-title {
    font-size: 34px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 20px;
}

.project-desc {
    font-size: 20px;
    line-height: 1.8;
    color: #475569;
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

.footer-box {
    background: white;

    padding: 35px;

    border-radius: 25px;

    margin-top: 50px;

    box-shadow:
    0 5px 20px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------

col1, col2 = st.columns([1, 4])

with col1:
    st.image(image)

with col2:
    st.markdown("""
    <div class="hero-container">

    <div class="hero-title">
    Dr. Samuel Israel
    </div>

    <div class="hero-subtitle">
    Healthcare AI | Data Scientist | Machine Learning Engineering |
    Clinical Intelligence | Digital Health Transformation
    </div>

    <div class="hero-text">

    Medical Doctor with 18+ years of clinical experience building
    deployable, executive-level Healthcare AI systems focused on:

    • Predictive Analytics<br>
    • Operational Intelligence<br>
    • Explainable AI<br>
    • Clinical Decision Support<br>
    • Healthcare Data Science<br>
    • Digital Health Transformation

    </div>

    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# METRICS SECTION
# -----------------------------

st.markdown('<div class="section-title">Executive Portfolio Highlights</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">3</div>
    <div class="metric-label">Flagship AI Platforms</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">18+</div>
    <div class="metric-label">Years Clinical Experience</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">10K+</div>
    <div class="metric-label">Healthcare Records Analyzed</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">AI</div>
    <div class="metric-label">Executive Intelligence Systems</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# PROJECTS SECTION
# -----------------------------

st.markdown('<div class="section-title">Flagship Healthcare AI Platforms</div>', unsafe_allow_html=True)

projects = [

 {
    "title": "🫀 CardioIntel AI",

    "desc": "Executive Cardiovascular Intelligence & Explainable Healthcare AI Platform integrating mortality prediction, SHAP explainability, biomarker intelligence, readmission prediction, and executive clinical dashboards.",

    "skills": [
        "SHAP AI",
        "Cardiovascular Analytics",
        "Mortality Prediction",
        "Clinical Decision Support"
    ],

    "live_link": "https://cardiointel-ai-8hvwda5isaw3auxwfkznni.streamlit.app/",

    "github_link": "https://github.com/drsam-israel/CardioIntel-AI"
},
   
   {
    "title": "🩺 DiaIntel AI",

    "desc": "Enterprise Diabetes Readmission Intelligence Platform focused on utilization analytics, occupancy forecasting, predictive healthcare intelligence, and executive operational dashboards.",

    "skills": [
        "Predictive AI",
        "Healthcare Forecasting",
        "Readmission Analytics",
        "Executive Dashboards"
    ],

    "live_link": "https://healthcare-executive-intelligence-platform-hhc25m9bn3etmvc6zgx.streamlit.app/",

    "github_link": "https://github.com/drsam-israel/healthcare-executive-intelligence-platform"
},

{
    "title": "🏥 HealthIntel AI",

    "desc": "Executive Healthcare Operations & Intelligence Platform developed for strategic KPI monitoring, operational analytics, patient trend intelligence, and healthcare transformation insights.",

    "skills": [
        "Healthcare KPIs",
        "Operational Intelligence",
        "Strategic Analytics",
        "Digital Health"
    ],

    "live_link": "https://healthcare-executive-intelligence-ai-platform-ersppv6rafg8uza7.streamlit.app/",

    "github_link": "https://github.com/drsam-israel/Healthcare-Executive-Intelligence-AI-Platform"
}

]

for project in projects:

    st.markdown(f"""
    <div class="project-card">

    <div class="project-title">
    {project['title']}
    </div>

    <div class="project-desc">
    {project['desc']}
    </div>

    <br>

    {" ".join([f'<span class="badge">{skill}</span>' for skill in project['skills']])}

    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])

    with c1:
        st.link_button(
            f"🔍 View Project — {project['title']}",
            project["live_link"],
            use_container_width=True
        )

    with c2:
        st.link_button(
            f"💻 GitHub — {project['title']}",
            project["github_link"],
            use_container_width=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
# -----------------------------
# PREMIUM FOOTER
# -----------------------------

st.markdown("""
<div class="footer-box">

<h2 style="
font-size:42px;
font-weight:800;
margin-bottom:25px;
color:#0f172a;
">
Building the Future of Healthcare Intelligence
</h2>

<p style="
font-size:22px;
line-height:2;
color:#475569;
">

This portfolio represents a growing ecosystem of deployable,
executive-level Healthcare AI systems designed to support:

<br><br>

• Clinical Intelligence<br>
• Predictive Healthcare Analytics<br>
• Explainable AI<br>
• Operational Decision Support<br>
• Healthcare Transformation<br>
• Executive Healthcare Strategy<br>
• Machine Learning Engineering<br>
• Data-driven Clinical Innovation

<br><br>

Focused on building real-world Healthcare AI solutions that bridge
clinical expertise, artificial intelligence, operational intelligence,
and digital health transformation.

</p>

</div>
""", unsafe_allow_html=True)