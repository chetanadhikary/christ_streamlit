import plotly.express as px


def department_distribution(df):
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

    return fig


def average_cgpa_by_department(df):
    cgpa_department = (
        df
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

    return fig

def placement_distribution(df):
    placement_data = (
        df["Placement_Status"]
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
    
    return fig