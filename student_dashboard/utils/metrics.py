import pandas as pd

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
    