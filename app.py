import streamlit as st

st.set_page_config(
    page_title="Heart Failure AI System",
    page_icon="❤️",
    layout="wide"
)

# Glassmorphism CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#0f172a,#312e81,#581c87);
    background-attachment: fixed;
}
.block {
    backdrop-filter: blur(15px);
    background: rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>❤️ Heart Failure Prediction System</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:white;'>Use sidebar pages to navigate Dashboard, Prediction & About</p>", unsafe_allow_html=True)

st.markdown("<div class='block'>🔍 Select a page from the left sidebar.</div>", unsafe_allow_html=True)
