import streamlit as st

#value = st.slider(0, 100, 50)

st.markdown("## Sample page")


values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.write("Test page")
