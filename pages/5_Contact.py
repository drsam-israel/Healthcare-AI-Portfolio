import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Contact | Dr. Samuel Israel",
    page_icon="📬",
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
# LOAD IMAGE
# ---------------------------------------------------

image = Image.open("assets/profile.png")
image = image.resize((180, 180))

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

.card:hover {

    transform: translateY(-8px);

    box-shadow:
    0 20px 40px rgba(0,0,0,0.15);

    border:
    1px solid #93c5fd;
}

.section-title {

    font-size: 30px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 20px;
}

.section-text {

    font-size: 20px;

    line-height: 1.9;

    color: #475569;
}

.contact-box {

    background: #eff6ff;

    padding: 25px;

    border-radius: 22px;

    margin-bottom: 20px;
}

.contact-title {

    font-size: 24px;

    font-weight: 700;

    color: #1d4ed8;

    margin-bottom: 10px;
}

.contact-text {

    font-size: 20px;

    color: #334155;
}

.footer-box {

    background:
    linear-gradient(
        135deg,
        #06122e 0%,
        #10245c 45%,
        #1d4ed8 100%
    );

    padding: 45px;

    border-radius: 35px;

    color: white;

    margin-top: 40px;
}

.footer-title {

    font-size: 40px;

    font-weight: 800;

    margin-bottom: 25px;
}

.footer-text {

    font-size: 22px;

    line-height: 2;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

col1, col2 = st.columns([1, 4])

with col1:
    st.image(image)

with col2:

    st.markdown("""
    <div class="title">
    Let's Connect
    </div>

    <div class="subtitle">

    Open to Healthcare AI collaborations,
    Healthcare Data Science opportunities,
    Digital Health Transformation projects,
    Clinical AI initiatives,
    and executive Healthcare AI innovation conversations.

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CONTACT SECTION
# ---------------------------------------------------

st.markdown("""
<div class="card">

<div class="section-title">
Professional Contact Information
</div>

<div class="section-text">

Connect for opportunities related to:

<br><br>

• Healthcare AI<br>
• Clinical AI Systems<br>
• Data Science<br>
• Machine Learning Engineering<br>
• Healthcare Analytics<br>
• Digital Health Transformation<br>
• Healthcare Innovation<br>
• Executive Healthcare Intelligence

</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CONTACT BOXES
# ---------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="contact-box">

    <div class="contact-title">
    🔗 LinkedIn
    </div>

    <div class="contact-text">
    www.linkedin.com/in/dr-samuel-israel-90893b228
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-box">

    <div class="contact-title">
    💻 GitHub
    </div>

    <div class="contact-text">
    https://github.com/drsam-israel?tab=repositories
    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="contact-box">

    <div class="contact-title">
    📧 Email
    </div>

    <div class="contact-text">
    samuelisraelpm@gmail.com
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-box">

    <div class="contact-title">
    📱 Phone
    </div>

    <div class="contact-text">
    0557326783, 09028784891
    </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CV SECTION
# ---------------------------------------------------

st.markdown("""
<div class="card">

<div class="section-title">
📄 Professional Resume / CV
</div>

<div class="section-text">

A downloadable executive Healthcare AI resume and portfolio CV
will be available here.

</div>

</div>
""", unsafe_allow_html=True)

with open("assets/cv/samuel_israel_cv.pdf", "rb") as file:
    st.download_button(
        label="⬇ Download CV",
        data=file,
        file_name="Dr_Samuel_Israel_Healthcare_AI_CV.pdf",
        mime="application/pdf"
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer-box">

<div class="footer-title">
Building Executive-Level Healthcare AI Systems
</div>

<div class="footer-text">

Focused on developing practical,
deployable,
and strategically aligned Healthcare AI solutions that combine:

<br><br>

• Clinical Expertise<br>
• Artificial Intelligence<br>
• Data Science<br>
• Machine Learning Engineering<br>
• Operational Intelligence<br>
• Explainable AI<br>
• Healthcare Analytics<br>
• Digital Health Transformation

<br><br>

Driving the future of intelligent healthcare systems through
data-driven innovation and executive Healthcare AI strategy.

</div>

</div>
""", unsafe_allow_html=True)