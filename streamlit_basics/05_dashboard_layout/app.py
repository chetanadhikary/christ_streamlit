import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)


# Load Data

df = pd.read_csv(
    "streamlit_basics/05_dashboard_layout/students.csv"
)


# Title

st.title("🎓 Student Analytics Dashboard")

st.write(
    """
    This module demonstrates dashboard design
    using Streamlit layout components.
    """
)


# Sidebar

st.sidebar.header("Dashboard Filters")


department = st.sidebar.selectbox(
    "Department",
    ["All"] + sorted(df["Department"].unique())
)


semester = st.sidebar.slider(
    "Semester",
    min_value=1,
    max_value=8,
    value=8
)


# Filtering

filtered_df = df


if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]


filtered_df = filtered_df[
    filtered_df["Semester"] <= semester
]


# Metrics

st.header("Overview")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Students",
        len(filtered_df)
    )


with col2:
    st.metric(
        "Average CGPA",
        round(filtered_df["CGPA"].mean(),2)
    )


with col3:

    placement = (
        len(
            filtered_df[
                filtered_df["Placement_Status"] == "Placed"
            ]
        )
        /
        len(filtered_df)
        * 100
    )

    st.metric(
        "Placement %",
        round(placement,2)
    )


# Data Table

st.header("Student Details")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# Charts

st.header("Analytics")


department_count = (
    filtered_df["Department"]
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
    title="Students by Department"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


placement_data = (
    filtered_df["Placement_Status"]
    .value_counts()
    .reset_index()
)


placement_data.columns = [
    "Status",
    "Count"
]


fig = px.pie(
    placement_data,
    names="Status",
    values="Count",
    title="Placement Status"
)


st.plotly_chart(
    fig,
    use_container_width=True
)