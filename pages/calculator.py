import streamlit as st

number1 = st.number_input('Insert a number 1: ')
number2 = st.number_input('Insert a number 2: ')
st.write('Addition: ', str(number1 + number2))
