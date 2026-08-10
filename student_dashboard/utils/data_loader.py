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
        missing_columns = set(required_columns) - set(df_student.columns)

        if missing_columns:
            st.error(
                f"missing columns {missing_columns}"
            )
            st.stop()
        return df_student
    except FileNotFoundError:
        return pd.DataFrame()

def get_metric(df:pd.DataFrame):
    """
    Gets the metrics from the loaded data

    args:
        dataframe containing students data

    Returns:
        dictionary containing metrics
    """
    dict_metrics = dict()
    
    if df is not None:
        average_cgpa=round(
            df["CGPA"].mean(),
            2
            )
        average_attendance = round(
            df["Attendance"].mean()
        )
        placement_percentage = round(
            (
                df["Placement_Status"]
                .value_counts(normalize=True)
                .get("Placed",0)
                *100
            ),
            2
        )
        dict_metrics["total_students"] = df.shape[0]
        dict_metrics["average_cgpa"] = average_cgpa
        dict_metrics["average_attendance"] = average_attendance
        dict_metrics["placement_status"] = placement_percentage
    return dict_metrics
    

if __name__ == "__main__":
    df = load_student_data("student_dashboard/data/students.csv")
    print(get_metric(df))
    