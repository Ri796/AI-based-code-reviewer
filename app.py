import streamlit as st

st.header("AI Driven Code Reviewer")  
st.subheader("Paste your code below")

st.text_area("Code Reviewer area", height=350, placeholder="paste the code here")

if st.button("Analyze"):
    st.write('Hello')