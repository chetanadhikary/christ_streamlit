import streamlit as st

st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀"
)

st.title("Welcome to Streamlit")

st.write(
    """
    This is my first Streamlit application.

    Streamlit allows us to create web applications
    using only Python.
    """
)

st.header("What we will learn")

st.markdown(
    """
    - Creating a Streamlit application
    - Displaying text
    - Adding user interaction
    - Working with data
    - Creating dashboards
    """
)

st.success(
    "Environment setup completed successfully!"
)