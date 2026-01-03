import streamlit as st

st.title("ℹ️ About Project")

st.write("""
This app predicts **heart failure risk** using machine learning.

Dataset source:  
Davide Chicco, Giuseppe Jurman (2020)
""")

st.markdown("---")

st.markdown(
    """
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:12px;
        color:white;
        font-family:Arial;
    ">
        <h3 style="color:#38bdf8;">🚀 Developer </h3>
        <p style="font-size:18px;">
            👤 <b style="color:#22c55e;">Arif Miah</b><br>
            🏢 <b style="color:#facc15;">Smart, Vision, AI</b><br>
            🌍 <b style="color:#e5e7eb;">Bangladesh</b>
        </p>
        <p style="font-size:14px; color:#94a3b8;">
            Machine Learning Engineer | AI Solutions
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
