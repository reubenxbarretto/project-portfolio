import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/reuben2.jpg")

with col2:
    st.title("Reuben Barretto")
    content = """
    I am Reuben Barretto a python programmer.i have graduated in  2025 with a 
    computer science degree. I am currently a student working on various projects.
    With a strong foundation in Python's extensive ecosystem, I've developed 
    expertise in various fields such as web development, data analysis,automation,
    and machine learning. I'm committed to continuous learning and staying up-to-date with the
    latest trends and technologies, ensuring that I'm always at the cutting edge of innovation. 
    Whether it's building robust applications or crafting efficient scripts,
    my meticulous attention to detail and creative approach help me
    deliver exceptional results and contribute effectively to any team.
    """
    st.info(content)

content2 = """
    Below you can find some of the apps i have built in python.Please feel free 
    to contact me
    """
st.write(content2)

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
