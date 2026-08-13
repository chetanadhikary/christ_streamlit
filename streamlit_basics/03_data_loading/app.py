import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Student Data Explorer",
    page_icon="📊"
)


st.title("📊 Student Data Explorer")

st.write(
    """
    In this module we learn how to load
    and explore data using Pandas.
    """
)


# Load CSV file

df = pd.read_csv(
    "streamlit_basics/03_data_loading/students.csv"
)


st.header("Student Dataset")

st.dataframe(
    df,
    use_container_width=True
)


st.header("Basic Information")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Students",
        len(df)
    )


with col2:
    st.metric(
        "Average CGPA",
        round(df["CGPA"].mean(), 2)
    )


with col3:
    placed = len(
        df[df["Placement_Status"] == "Placed"]
    )

    percentage = round(
        placed / len(df) * 100,
        2
    )

    st.metric(
        "Placement %",
        percentage
    )


st.header("Filter Students")


department = st.selectbox(
    "Select Department",
    ["All"] + sorted(df["Department"].unique())
)


filtered_df = df


if department != "All":
    filtered_df = df[
        df["Department"] == department
    ]


st.dataframe(
    filtered_df,
    use_container_width=True
)