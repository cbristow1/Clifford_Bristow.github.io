import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


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
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("How's it going my names Clifford Bristow:wave:")
    st.title("An up and coming Programmer learning Python from, Oklahoma City")
    st.write(
        "I am passionate about finding ways to use Python in the field of Finance and Investment Management."
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
            I’ve spent the last 15+ years working with leading influential change agents. 
            Today, I am an achieved Business Administration Professional with experience in data governance project 
            coordination and management, showcasing a strong record of analytical prowess. My experience has allowed 
            me to develop strong business acumen and organizational strategies that strengthen client relations, communications development, 
            and operational outcomes.

        I enjoy generating new ideas and devising feasible solutions to 
        broadly relevant problems, especially in the world of data governance, 
        risk management, and financial services. My colleagues and 
        employers describe me as a persuasive, venturesome individual who maintains 
        a confident and proactive attitude when faced with adversity.

Please  feel free to contact me at Clifford.bristow@gmail.com as I welcome the opportunity to connect and discuss how my experience and background may be 
requested for any speaking opportunities and/or unique business needs.

Core Competencies:

- Risk Management 
- Business Intelligence 
- Federal Data Governance & Compliance:
            "

            If you're interested in learning more about be fill out 
            the reach out to part of the page.
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
    # with image_column:
    #     st.image(img_lottie_animation)
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
