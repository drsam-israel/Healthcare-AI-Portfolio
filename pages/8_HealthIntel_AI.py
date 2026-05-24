import streamlit as st

st.set_page_config(
    page_title="HealthIntel AI",
    page_icon="🏥",
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
    background: linear-gradient(135deg, #0f172a, #1e293b, #1e3a8a);
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
    background: #eff6ff;
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #bfdbfe;
}

.metric h2 {
    color: #1d4ed8;
    font-size: 34px;
    font-weight: 900;
}

.metric p {
    color: #475569;
    font-size: 16px;
}

.badge {
    display: inline-block;
    background: #dbeafe;
    color: #1d4ed8;
    padding: 8px 16px;
    border-radius: 22px;
    margin: 5px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🏥 HealthIntel AI</h1>
<p>
Executive Healthcare Operations & Intelligence Platform designed for
healthcare KPI monitoring, operational analytics,
patient trend intelligence, executive healthcare visibility,
and digital health transformation.
</p>
</div>
""", unsafe_allow_html=True)

st.image("assets/screenshots/healthintel.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown('<div class="metric"><h2>KPI</h2><p>Executive Monitoring</p></div>', unsafe_allow_html=True)

with m2:
    st.markdown('<div class="metric"><h2>BI</h2><p>Operational Analytics</p></div>', unsafe_allow_html=True)

with m3:
    st.markdown('<div class="metric"><h2>AI</h2><p>Healthcare Intelligence</p></div>', unsafe_allow_html=True)

with m4:
    st.markdown('<div class="metric"><h2>DX</h2><p>Digital Transformation</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Business Challenge</h2>
<p>
Healthcare executives require integrated intelligence systems capable of monitoring:
operational KPIs,
capacity visibility,
patient trends,
strategic healthcare analytics,
and healthcare system performance.
Many traditional systems remain fragmented and reactive.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>AI Solution</h2>
<p>
HealthIntel AI was developed as an Executive Healthcare Operations &
Intelligence Platform integrating operational analytics,
executive dashboards,
patient trend intelligence,
healthcare KPI monitoring,
and strategic healthcare visibility.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Core Capabilities</h2>
<p>
• Executive KPI dashboards<br>
• Operational healthcare analytics<br>
• Strategic healthcare intelligence<br>
• Patient trend monitoring<br>
• Healthcare operations visibility<br>
• Data-driven healthcare insights<br>
• Digital transformation intelligence
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Technology Stack</h2>
<span class="badge">Python</span>
<span class="badge">Streamlit</span>
<span class="badge">Healthcare Analytics</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Business Intelligence</span>
<span class="badge">Executive Dashboards</span>
<span class="badge">Digital Health</span>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View Live Project",
        "https://healthcare-executive-intelligence-ai-platform-ersppv6rafg8uza7.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/Healthcare-Executive-Intelligence-AI-Platform"
    )

st.success(
    "HealthIntel AI demonstrates executive-level healthcare operational intelligence powered by Healthcare AI and strategic analytics."
)