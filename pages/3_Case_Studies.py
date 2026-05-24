import streamlit as st

st.set_page_config(
    page_title="Healthcare AI Case Studies",
    page_icon="📊",
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

.case-card {

    background: white;

    padding: 40px;

    border-radius: 30px;

    margin-bottom: 40px;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.08);

    border:
    1px solid #e2e8f0;

    transition: all 0.35s ease;

    cursor: pointer;
}

.case-card:hover {

    transform: translateY(-8px);

    box-shadow:
    0 20px 40px rgba(0,0,0,0.15);

    border:
    1px solid #93c5fd;
}
.case-title {

    font-size: 40px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 25px;
}

.section-header {

    font-size: 26px;

    font-weight: 700;

    color: #1d4ed8;

    margin-top: 25px;

    margin-bottom: 15px;
}

.case-text {

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
# PAGE HEADER
# ---------------------------------------------------

st.markdown("""
<div class="title">
Healthcare AI Case Studies
</div>

<div class="subtitle">

Executive-level Healthcare AI systems developed to support predictive analytics,
operational intelligence, explainable AI, strategic healthcare analytics,
and healthcare transformation.

</div>
""", unsafe_allow_html=True)

# =====================================================
# CARDIOINTEL AI
# =====================================================

st.markdown("""
<div class="case-card">

<div class="case-title">
🫀 CardioIntel AI
</div>

<div class="section-header">
Business Challenge
</div>

<div class="case-text">

Healthcare systems require proactive cardiovascular intelligence systems capable of supporting:
mortality surveillance,
biomarker intelligence,
readmission risk prediction,
clinical decision support,
and executive healthcare analytics.

Traditional reporting systems often lack predictive visibility and explainable AI capabilities.

</div>

<div class="section-header">
AI Solution
</div>

<div class="case-text">

Developed an Executive Cardiovascular Intelligence & Explainable Healthcare AI Platform
integrating predictive analytics, SHAP explainability, operational dashboards,
mortality intelligence, and executive healthcare monitoring systems.

</div>

<div class="section-header">
Key Capabilities
</div>

<div class="case-text">

• Mortality Risk Prediction<br>
• Biomarker Intelligence<br>
• SHAP Explainable AI<br>
• Readmission Surveillance<br>
• Executive KPI Dashboards<br>
• Clinical Decision Support<br>
• Operational Intelligence

</div>

<div class="section-header">
Strategic Impact
</div>

<div class="case-text">

Enabled executive-level cardiovascular intelligence visibility,
improved operational awareness,
supported data-driven healthcare decision-making,
and demonstrated deployable Healthcare AI capabilities.

</div>

<br>

<span class="badge">Healthcare AI</span>
<span class="badge">Cardiovascular Analytics</span>
<span class="badge">SHAP Explainability</span>
<span class="badge">Mortality Prediction</span>
<span class="badge">Executive Dashboards</span>

</div>
""", unsafe_allow_html=True)

# =====================================================
# DIAINTEL AI
# =====================================================

st.markdown("""
<div class="case-card">

<div class="case-title">
🩺 DiaIntel AI
</div>

<div class="section-header">
Business Challenge
</div>

<div class="case-text">

Healthcare organizations continue to experience challenges related to:
diabetes readmissions,
utilization burden,
operational inefficiencies,
capacity strain,
and fragmented operational intelligence.

Many traditional systems lack predictive healthcare visibility and executive operational analytics.

</div>

<div class="section-header">
AI Solution
</div>

<div class="case-text">

Developed an Enterprise Diabetes Readmission Intelligence &
Predictive Healthcare AI Platform integrating:
predictive analytics,
occupancy forecasting,
operational healthcare intelligence,
executive dashboards,
and healthcare KPI monitoring.

</div>

<div class="section-header">
Key Capabilities
</div>

<div class="case-text">

• Diabetes Utilization Analytics<br>
• Readmission Prediction<br>
• Operational Intelligence<br>
• Occupancy Forecasting<br>
• Executive KPI Monitoring<br>
• Strategic Healthcare Analytics

</div>

<div class="section-header">
Strategic Impact
</div>

<div class="case-text">

Demonstrated how deployable Healthcare AI systems can support operational healthcare visibility,
improve executive intelligence,
and strengthen healthcare transformation initiatives.

</div>

<br>

<span class="badge">Predictive Healthcare AI</span>
<span class="badge">Operational Intelligence</span>
<span class="badge">Healthcare Forecasting</span>
<span class="badge">Executive Analytics</span>
<span class="badge">Healthcare KPIs</span>

</div>
""", unsafe_allow_html=True)

# =====================================================
# HEALTHINTEL AI
# =====================================================

st.markdown("""
<div class="case-card">

<div class="case-title">
🏥 HealthIntel AI
</div>

<div class="section-header">
Business Challenge
</div>

<div class="case-text">

Healthcare executives require integrated operational intelligence systems capable of monitoring:
patient trends,
operational KPIs,
capacity visibility,
strategic analytics,
and healthcare performance metrics.

Many systems remain fragmented and reactive.

</div>

<div class="section-header">
AI Solution
</div>

<div class="case-text">

Developed an Executive Healthcare Operations &
Intelligence Platform focused on strategic healthcare analytics,
operational intelligence,
KPI monitoring,
patient trend analysis,
and executive healthcare visibility.

</div>

<div class="section-header">
Key Capabilities
</div>

<div class="case-text">

• Healthcare KPI Monitoring<br>
• Operational Analytics<br>
• Strategic Dashboards<br>
• Patient Trend Intelligence<br>
• Executive Healthcare Visibility<br>
• Digital Health Intelligence

</div>

<div class="section-header">
Strategic Impact
</div>

<div class="case-text">

Showcased how Healthcare AI and operational analytics can support healthcare transformation,
executive visibility,
strategic planning,
and data-driven healthcare leadership.

</div>

<br>

<span class="badge">Healthcare Operations</span>
<span class="badge">Operational Analytics</span>
<span class="badge">Executive Intelligence</span>
<span class="badge">Healthcare Transformation</span>
<span class="badge">Strategic Dashboards</span>

</div>
""", unsafe_allow_html=True)

st.success(
    "Executive Healthcare AI case studies demonstrating deployable, strategic, and operational healthcare intelligence systems."
)