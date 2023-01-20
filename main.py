# This will be the main entry point for your Streamlit app.

import streamlit as st

st.title("Hello World!")

with st.expander("Click here to learn more"):
    st.write(
        "This is a Streamlit app template. It's a good starting point for building Streamlit apps."
    )
