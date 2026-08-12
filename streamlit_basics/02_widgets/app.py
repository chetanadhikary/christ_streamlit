import streamlit as st


st.set_page_config(
    page_title="Student Profile Generator",
    page_icon="🎓"
)


st.title("🎓 Student Profile Generator")

st.write(
    """
    This application demonstrates Streamlit widgets.
    Enter your details below.
    """
)


# Text input
name = st.text_input(
    "Enter your name"
)


# Dropdown selection
department = st.selectbox(
    "Select your department",
    [
        "Computer Science",
        "Artificial Intelligence",
        "Electronics",
        "Mechanical",
        "Civil"
    ]
)


# Slider input
semester = st.slider(
    "Select your semester",
    min_value=1,
    max_value=8,
    value=1
)


# Radio button
interested_area = st.radio(
    "Your area of interest",
    [
        "Data Science",
        "Artificial Intelligence",
        "Web Development",
        "Cyber Security"
    ]
)


# Button action
if st.button("Generate Profile"):

    st.success("Profile Generated!")

    st.subheader("Student Details")

    st.write(
        f"""
        **Name:** {name}

        **Department:** {department}

        **Semester:** {semester}

        **Interest:** {interested_area}
        """
    )