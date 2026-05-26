import streamlit as st

st.set_page_config(
    page_title="Healthcare Operations Command Center",
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
<h1>🏥 Healthcare Operations Command Center</h1>
<p>
Enterprise Healthcare Operations Intelligence System designed for
real-world hospital workflow analytics, bed occupancy monitoring,
ICU utilization intelligence, patient flow analytics,
length-of-stay insights, operational forecasting,
executive KPI tracking, and healthcare decision support.
</p>
</div>
""", unsafe_allow_html=True)

st.info("Executive Operations Dashboard screenshot will be added here.")

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown('<div class="metric"><h2>LOS</h2><p>Length-of-Stay Analytics</p></div>', unsafe_allow_html=True)

with m2:
    st.markdown('<div class="metric"><h2>ICU</h2><p>ICU Utilization Intelligence</p></div>', unsafe_allow_html=True)

with m3:
    st.markdown('<div class="metric"><h2>OPS</h2><p>Operational Intelligence</p></div>', unsafe_allow_html=True)

with m4:
    st.markdown('<div class="metric"><h2>KPI</h2><p>Executive Command Center</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Business Challenge</h2>
<p>
Healthcare organizations continue to face increasing operational pressure related to:
ICU congestion,
bed occupancy strain,
prolonged patient length of stay,
inefficient patient flow,
emergency department overcrowding,
delayed discharge coordination,
fragmented operational visibility,
and rising operational costs.
Many traditional reporting systems remain reactive and lack integrated command-center intelligence.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>AI / Analytics Solution</h2>
<p>
The Healthcare Operations Command Center was developed as a deployable enterprise healthcare
operations intelligence environment integrating hospital workflow analytics,
patient flow intelligence,
bed occupancy monitoring,
ICU utilization analytics,
length-of-stay insights,
operational forecasting,
executive KPI tracking,
and healthcare decision support.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Core Capabilities</h2>
<p>
• Executive healthcare operations dashboards<br>
• Bed occupancy monitoring<br>
• ICU utilization intelligence<br>
• Patient flow analytics<br>
• Length-of-stay analytics<br>
• ED congestion monitoring<br>
• Operational forecasting<br>
• Capacity pressure intelligence<br>
• Healthcare KPI tracking<br>
• Executive decision support
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>Technology Stack</h2>
<span class="badge">Python</span>
<span class="badge">Streamlit</span>
<span class="badge">Pandas</span>
<span class="badge">Plotly</span>
<span class="badge">Healthcare Analytics</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Executive Dashboards</span>
<span class="badge">Command Center</span>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "🔍 View Live Project",
        "https://enterprise-healthcare-operations-intelligence-system-kxqd4qjp6.streamlit.app/"
    )

with c2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/drsam-israel/enterprise-healthcare-operations-intelligence-system"
    )

st.success(
    "Healthcare Operations Command Center demonstrates enterprise-level hospital workflow analytics, operational intelligence, and executive healthcare decision support."
)