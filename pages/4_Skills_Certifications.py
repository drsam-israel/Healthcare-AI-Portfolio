import streamlit as st

st.set_page_config(
    page_title="Skills & Certifications",
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
# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f4f7fb;
}

.title {
    font-size: 58px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 15px;
}

.subtitle {
    font-size: 22px;
    color: #475569;
    line-height: 1.8;
    margin-bottom: 45px;
}

.card {

    background: white;

    padding: 35px;

    border-radius: 28px;

    margin-bottom: 30px;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.08);

    border:
    1px solid #e2e8f0;

    transition: all 0.35s ease;

    cursor: pointer;
}

.card:hover {

    transform: translateY(-8px);

    box-shadow:
    0 20px 40px rgba(0,0,0,0.15);

    border:
    1px solid #93c5fd;
}
.card-title {

    font-size: 30px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 20px;
}

.card-text {

    font-size: 20px;

    line-height: 1.9;

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

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
<div class="title">
Skills & Certifications
</div>

<div class="subtitle">

Healthcare AI, Data Science, Machine Learning Engineering,
Healthcare Analytics, Digital Health Transformation,
and Executive Healthcare Intelligence capabilities.

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SKILLS SECTION
# ---------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🧠 Healthcare AI & Data Science
    </div>

    <div class="card-text">

    • Healthcare AI<br>
    • Predictive Analytics<br>
    • Clinical Intelligence<br>
    • Explainable AI (SHAP)<br>
    • Healthcare Data Science<br>
    • Machine Learning Engineering<br>
    • Healthcare Analytics<br>
    • Clinical Decision Support

    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    💻 Technical Skills
    </div>

    <div class="card-text">

    • Python<br>
    • Streamlit<br>
    • Data Visualization<br>
    • Dashboard Development<br>
    • Machine Learning<br>
    • Deep Learning<br>
    • Executive KPI Analytics<br>
    • Operational Intelligence Systems

    </div>

    </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    📊 Analytics & Strategy
    </div>

    <div class="card-text">

    • Healthcare KPI Monitoring<br>
    • Business Intelligence<br>
    • Data Storytelling<br>
    • Operational Analytics<br>
    • Strategic Healthcare Analytics<br>
    • Healthcare Transformation<br>
    • AI Strategy<br>
    • Executive Decision Support

    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🏥 Healthcare & Leadership
    </div>

    <div class="card-text">

    • Digital Health Transformation<br>
    • Clinical Workflow Understanding<br>
    • Healthcare Operations<br>
    • AI Governance<br>
    • Product Thinking<br>
    • Agile & Scrum Exposure<br>
    • Healthcare Innovation<br>
    • Executive Communication

    </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------

st.markdown("""
<div class="card">

<div class="card-title">
📜 Certifications & Professional Training
</div>

<div class="card-text">

• Advanced Certification in Data Science & AI — IIT / Intellipaat<br><br>

• AI Certification in Healthcare — Digital Health Africa (DHA)<br><br>

• Certified Scrum Product Owner (CSPO) — Scrum Alliance<br><br>

• Data Analytics & Product Management — InternPulse<br><br>

• Project Management Training — 3P Consulting<br><br>

• Business Analysis Training US Healthcare System — Techcanvass<br><br>



</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# BADGES
# ---------------------------------------------------

st.markdown("""
<span class="badge">Healthcare AI</span>
<span class="badge">Data Science</span>
<span class="badge">Machine Learning</span>
<span class="badge">Digital Health</span>
<span class="badge">Healthcare Analytics</span>
<span class="badge">Explainable AI</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Healthcare Transformation</span>
<span class="badge">AI Strategy</span>
<span class="badge">Clinical Intelligence</span>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.success(
    "Premium Healthcare AI capability portfolio combining clinical expertise, artificial intelligence, analytics, and digital transformation."
)