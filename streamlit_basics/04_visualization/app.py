import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Student Analytics",
    page_icon="📊"
)


st.title("📊 Student Data Visualization")


df = pd.read_csv(
    "streamlit_basics/04_visualization/students.csv"
)


st.header("Student Data")

st.dataframe(
    df,
    use_container_width=True
)


# Department wise student count

st.subheader("Students by Department")


department_count = (
    df["Department"]
    .value_counts()
    .reset_index()
)

department_count.columns = [
    "Department",
    "Students"
]


fig = px.bar(
    department_count,
    x="Department",
    y="Students",
    title="Number of Students by Department"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# CGPA distribution

st.subheader("CGPA Distribution")


fig = px.histogram(
    df,
    x="CGPA",
    nbins=5,
    title="Student CGPA Distribution"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# Placement status

st.subheader("Placement Status")


placement = (
    df["Placement_Status"]
    .value_counts()
    .reset_index()
)

placement.columns = [
    "Status",
    "Count"
]


fig = px.pie(
    placement,
    names="Status",
    values="Count",
    title="Placement Distribution"
)


st.plotly_chart(
    fig,
    use_container_width=True
)