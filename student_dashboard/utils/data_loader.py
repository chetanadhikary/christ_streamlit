import pandas as pd
import streamlit as st

def load_student_data(file_path):
    """
    Load student data from CSV file

    args:
        file_path: Path to csv file

    Returns:
        pandas dataframe
    """
    try:
        df_student = pd.read_csv(file_path)
        return df_student
    except FileNotFoundError:
        return pd.DataFrame()

def validate_columns(df):
    required_columns = [
                "Student_ID",
                "Name",
                "Department",
                "Semester",
                "CGPA",
                "Attendance",
                "Programming_Score",
                "Placement_Status"
            ]
    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        return False,missing_columns

    return True,None



if __name__ == "__main__":
    df = load_student_data("student_dashboard/data/students.csv")
    print(get_metric(df))
    