import streamlit as st
import plotly.express as px
from utils.data_loader import load_student_data,get_metric

# Page configuration
st.set_page_config(page_title="Student Analytics Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide")

# Application Title
st.title("Student Analytics Dashboard")

st.write("""
    Welcome to Student Analytics Dashboard.

    This demonstrates pandas and streamlit capabilites
""")

st.sidebar.header("Dashboard Controls")

st.sidebar.info(""" 
Filters and controls will appear here"""
)

# Main sections

st.header("Student Data Overview")

st.info("""
Student dataset will be loaded here"""
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Student CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    df_student = load_student_data(uploaded_file)
    st.sidebar.success(
        "Using uploaded dataset"
    )
else:
    DATA_FILE = "student_dashboard/data/students.csv"
    df_student = load_student_data(DATA_FILE)
    st.sidebar.info(
        "using sample dataset"
    )


st.sidebar.header("Filters")

if df_student is not None:
    departments = [
        "All"
    ] + sorted(
        df_student["Department"].unique().tolist()
    )

    selected_department = st.sidebar.selectbox(
        "Select Department",
        departments
    )

    semesters = [
        "All"
    ]+ sorted(
        df_student["Semester"].unique().tolist()
    )
    selected_semester = st.sidebar.selectbox(
        "Select a Semester",
        semesters
    )

df_filtered = df_student.copy()

if selected_department != "All":
    df_filtered = df_filtered[
        df_filtered["Department"] == selected_department
    ]

if selected_semester != "All":
    df_filtered = df_filtered["Semester"] == selected_semester


min_cgpa = st.sidebar.slider(
    "Minimum CGPA",
    min_value=float(df_filtered["CGPA"].min()),
    max_value=float(df_filtered["CGPA"].max()),
    value=7.0
)

df_filtered = df_filtered[
    df_filtered["CGPA"] >= min_cgpa
]

st.header("Analytics")

st.dataframe(df_filtered,use_container_width=True)

dict_metrics = get_metric(df=df_filtered)

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Students",
        value= dict_metrics.get("total_students","--")
    )

with col2:
    st.metric(
        label="Average CGPA",
        value= dict_metrics.get("average_cgpa","--")
    )

with col3:
    st.metric(
        label="Placement %",
        value= dict_metrics.get("placement_status","--")
    )

st.header("Visualizations")
st.write(
    "Charts will be deplayed here"
)

st.subheader("Students by Department")


department_count = (
    df_filtered["Department"]
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

st.subheader("Average CGPA by Department")

cgpa_department = (
    df_filtered
    .groupby("Department")["CGPA"]
    .mean()
    .reset_index()
)

fig = px.bar(
    cgpa_department,
    x="Department",
    y="CGPA",
    title="Average CGPA Department-wise"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader("Placement Status")

placement_data = (
    df_filtered["Placement_Status"]
    .value_counts()
    .reset_index()
)
placement_data.columns = [
    "Status",
    "Count"
]

fig=px.pie(
    placement_data,
    names="Status",
    values="Count",
    title="Placement Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Footer
st.divider()

st.caption(
    "Built using Python and Streamlit"
)