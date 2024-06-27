import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/reuben.jpg")

with col2:
    st.title("Reuben Barretto")
    content = """
    I am Reuben Barretto a python programmer.i have graduated in  2025 with a 
    computer science degree. I am currently a student working on various projects
    """
    st.info(content)
