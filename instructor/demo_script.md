# Streamlit Workshop - Instructor Demo Script

## Purpose

This document guides the instructor through live demonstrations.

The goal is not only to show code, but to explain the thinking process behind building data applications.

---

# Opening Demo (Before Module 1)

## Objective

Create excitement and show the final destination.

---

## Demo

Open the deployed Student Analytics Dashboard.

Show:

- Dashboard layout
- Filters
- Metrics
- Charts


Ask students:

> "How many lines of Python do you think are required to create something like this?"

Allow guesses.


Explain:

"Today we will build this step-by-step. Each module contributes one piece."


---

# Module 1 Demo

## Hello Streamlit


Open:
```bash
streamlit_basics/01_hello_streamlit/app.py
```

Explain:

"Streamlit converts Python scripts into interactive web applications."


Live coding:

```python
import streamlit as st

st.title("My First Streamlit App")

st.write("Hello World")
```

Student activity:

Modify:

* Title
* Description
* Content

Checkpoint:

Every student should see their own application.

# Module 2 Demo

### Widgets and Interaction

Open:
```bash
streamlit_basics/02_widgets
```
Explain:

“Widgets allow users to communicate with our Python program.”

Demonstrate:

### Text Input
```python
name = st.text_input(
    "Enter your name"
)
```
Explain:

“The value entered by the user becomes a Python variable.”

### Dropdown

```python
department = st.selectbox(
    "Department",
    [
        "CSE",
        "AI",
        "ECE"
    ]
)
```
Explain:

“Applications become dynamic based on user choices.”

### Slider
```python
cgpa = st.slider(
    "CGPA",
    0.0,
    10.0
)
```

Student Challenge:

Create a student profile application.

# Module 3 Demo

### Working With Data

Open:
```python
streamlit_basics/03_data_loading
```

Explain:
"Most real applications are data-driven.”

Show:
```
CSV file
↓
Pandas DataFrame
↓
Streamlit Display
```

Live Coding:
```python
Python
df = pd.read_csv(
    "students.csv"
)
st.dataframe(df)
```

Explain:
"Streamlit automatically converts data into a web table."

Demonstrate filtering:
```python
Python
df[df["CGPA"] > 8]
```
# Module 4 Demo

### Visualization

Open:
```bash
streamlit_basics/04_visualization
```

Explain:

“Charts are not decoration. They communicate insights.”

Show:

Raw data:


| Department | Students |
|------------|----------|
|  CSE           | 120|
|  AI            | 80|
|  ECE           | 100|

Convert to chart:
```python
Python
px.bar(
    data,
    x="Department",
    y="Studets"
)
```

Explain:

"Good dashboards answer questions."

Examples:

* Which department has more students?
* What is the average performance?
* What trends exist?

# Module 5 Demo

### Dashboard Architecture

Open:
```bash
streamlit_basics/05_dashboard_layout
```

Explain:

"A dashboard is a combination of components."

Show architecture:
```
Sidebar

   |
   |
Filters


Main Area

   |
   |
Metrics

   |
   |
Charts
```

Demonstrate:

### Columns
```python
Python
col1,col2 = st.columns(2)
```

### Metrics
```python
Python
st.metric(
    "Average CGPA",
    "8.5"
)
```

Explain
 
" Important information should be visible immediately."

# Final Project Demo

### Transition

“Now you have all the building blocks. It is your turn to create the application.”

Students open:
```bash
final_project
```

Requirements:

1. Load data
2. Add filters
3. Display metrics
4. Add charts



