#!/usr/bin/env python3py

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image

cwd = Path.cwd()

# env vars
contact_form = f"{cwd}/images/Profile Picture.jpeg"

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="My Webpage",
    page_icon=":tada:",
    layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ruflv73p.json")
#img_contact_form = Image.open(contact_form)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("How's it going my name's Clifford Bristow:wave:")
    st.title("An up and coming Data Analyst learning Python from Oklahoma City")
    st.write(
        "🏢 Data-Focused Operations Leader 📋 Lifecycle Management 🤝 Quantitative Analysis 🎈 Business Intelligence Solutions 📈 Root Cause Analysis"
    )
    st.write("[Learn More >](https://www.linkedin.com/in/clifford-bristow-mba-cc-lion/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#####")
        st.write(
            """
            Data-focused leader offering 15+ years driving organizational performance, business insight and strategic growth 
            through enterprise data strategy development and execution. Extensive expertise performing thorough evaluation of business systems, 
            data integration, advanced analytics adoption, governance protocols, and reporting metrics translating into actionable insights.

            Spearheaded multiple high-impact initiatives implementing methods to enhance data collection, machine learning, quantitative modeling, 
            and mining revealing trends and opportunities for product and service line improvement. Implemented a data driven strategy that continuously 
            decreased loans overdue by +2% from November ‘Y19 till present.

            Future-focused decision makers are able to clearly convey complex data findings, roadmaps and next steps through compelling translations and 
            visualizations to senior leadership. Dedicated stakeholder partner who progresses KPIs and solutions through collaborative work groups and aligning 
            data-use policies across business units achieving 98% accuracy.

            Passionate about leveraging data, analytics, and visibility to accelerate growth. Seeking to bring strengths in process enhancements, project leadership, 
            operational streamlining, and strategic alignment of systems to a forward-thinking organization. My top skills include Python, Power BI, advanced statistical analysis, 
            AWS cloud solutions, stakeholder engagement and team mentoring.

            Are you seeking to inject more data-driven decision making into your organization? Does your team need an expert in data integration, advanced analytics adoption, and governance protocol implementation? 
            Contact me to discuss how my expertise can enable fact-based strategies to reduce risks and seize opportunities through business intelligence platforms and data modeling. I am eager to partner with 
            visionary leaders who want to build insight-fueled, performance-driven enterprises poised for the future through data analytics maturity.

            I look forward to meeting you! You can reach me at clifford.bristow@gmail.com.
            """
        )
        st.write("[ >]()")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("COMING SOON")
        st.write(
            """

            """
        )
        st.markdown("")
with st.container():
    image_column, text_column = st.columns((1, 2))
    # with image_column:
    #     st.image(img_contact_form)
    with text_column:
        st.subheader("")
        st.write(
            """

            """
        )
        st.markdown("[]()")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/clifford.bristow@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
