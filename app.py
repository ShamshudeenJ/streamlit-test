import streamlit as st

value = st.slider(0, 100, 50)

st.write(f"Slider value: {value}")
