import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About | Dr. Samuel Israel",
    page_icon="👨‍⚕️",
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

st.markdown("""
<style>
.main { background-color: #f4f7fb; }

.title {
    font-size: 58px;
    font-weight: 800;
    color: #0f172a;
}

.subtitle {
    font-size: 22px;
    color: #475569;
    line-height: 1.8;
    margin-bottom: 40px;
}

.card {

    background: white;

    padding: 35px;

    border-radius: 28px;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.08);

    border:
    1px solid #e2e8f0;

    margin-bottom: 30px;

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
.card h3 {
    color: #0f172a;
    font-size: 30px;
    font-weight: 800;
}

.card p, .card li {
    color: #475569;
    font-size: 19px;
    line-height: 1.9;
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

image = Image.open("assets/profile.png")
image = image.resize((180, 180))

col1, col2 = st.columns([1, 4])

with col1:
    st.image(image)

with col2:
    st.markdown("""
    <div class="title">About Dr. Samuel Israel</div>
    <div class="subtitle">
    Medical Doctor | Healthcare AI Specialist | Data Scientist | Machine Learning Engineering | Clinical Intelligence | Digital Health Transformation
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>Professional Profile</h3>
<p>
Medical Doctor with 18+ years of clinical experience and advancing expertise in Healthcare AI, Data Science,
Machine Learning Engineering, Clinical Intelligence, Healthcare Analytics, Digital Health Transformation,
AI Governance, and deployable executive-level healthcare technology solutions.
</p>
<p>
My work focuses on building practical Healthcare AI systems that move beyond theory into real-world clinical,
operational, and executive intelligence.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>Healthcare AI Mission</h3>
<p>
To build responsible, explainable, and deployable Healthcare AI systems that support better clinical decisions,
improve operational visibility, strengthen healthcare analytics, and accelerate digital health transformation.
</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>Clinical Foundation</h3>
    <p>
    18+ years of medical and healthcare experience, providing strong domain understanding of clinical workflows,
    patient care, healthcare operations, and real-world healthcare decision-making.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>AI & Data Science</h3>
    <p>
    Building skills across Python, machine learning, predictive analytics, explainable AI, healthcare dashboards,
    data storytelling, and AI-powered decision support systems.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>Digital Health Strategy</h3>
    <p>
    Focused on applying AI, analytics, product thinking, and transformation strategy to healthcare systems,
    operations, patient outcomes, and executive decision-making.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>Education</h3>
<ul>
<li><b>MIVA Master of Information Technology (MIT), AI Specialization</b></li>
<li><b>Bachelor of Medicine, Bachelor of Surgery (MB,BS),</b> — Ebonyi State University</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>Core Positioning</h3>
<span class="badge">Healthcare AI</span>
<span class="badge">Data Science</span>
<span class="badge">Machine Learning Engineering</span>
<span class="badge">Clinical Intelligence</span>
<span class="badge">Explainable AI</span>
<span class="badge">Digital Health Transformation</span>
<span class="badge">Healthcare Analytics</span>
<span class="badge">AI Strategy</span>
</div>
""", unsafe_allow_html=True)