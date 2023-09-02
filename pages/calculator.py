import streamlit as st

number1 = st.number_input('Insert a number')
number2 = st.number_input('Insert a number')
st.write('Addition: ', str(number1 + number2))
