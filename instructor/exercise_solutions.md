# Streamlit Workshop - Exercise Solutions

This document contains suggested solutions for workshop exercises.

---

# Module 1: Hello Streamlit

## Exercise

Modify the application:

- Change title
- Add student information
- Add description


## Suggested Solution

```python
st.title("Welcome to CHRIST Streamlit Workshop")

st.write(
"""
This application demonstrates
building web applications using Python.
"""
)

# Module 2: Widgets

## Exercise

Create a student profile application.

Required:

* Name
* Department
* CGPA
* Interest

## Suggested Solution

```python

name = st.text_input(
    "Student Name"
)


department = st.selectbox(
    "Department",
    [
        "CSE",
        "AI",
        "ECE",
        "Mechanical"
    ]
)


cgpa = st.slider(
    "CGPA",
    0.0,
    10.0,
    7.0
)


interest = st.radio(
    "Interest",
    [
        "AI",
        "Data Science",
        "Cloud"
    ]
)

# Module 3: Data Loading

## Exercise

### Add CGPA filtering.


```python
minimum_cgpa = st.slider(
    "Minimum CGPA",
    0.0,
    10.0,
    7.0
)


filtered_df = df[
    df["CGPA"] >= minimum_cgpa
]

### Add placement filter:

```python
status = st.selectbox(
    "Placement Status",
    [
        "All",
        "Placed",
        "Not Placed"
    ]
)


if status != "All":

    filtered_df = filtered_df[
        filtered_df["Placement_Status"] == status
    ]

# Module 4 : Visualization

## Exercise

Create department CGPA analysis.

### Suggested Solution

```python
cgpa_department = (
    df.groupby("Department")["CGPA"]
    .mean()
    .reset_index()
)


fig = px.bar(
    cgpa_department,
    x="Department",
    y="CGPA",
    title="Average CGPA by Department"
)


st.plotly_chart(fig)

# Module 5: Dashboard

## Exercise

Add another KPI

### Example

Highest CGPA

### Suggested Solution

```python
highest_cgpa = df["CGPA"].max()


st.metric(
    "Highest CGPA",
    highest_cgpa
)