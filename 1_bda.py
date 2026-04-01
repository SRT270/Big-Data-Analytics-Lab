#  Descriptive, Diagnostic, Predictive, and Prescriptive—to student performance and resource allocation.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from pulp import LpMaximize, LpProblem, LpVariable

# 1. DESCRIPTIVE ANALYTICS: "What Happened?"
def descriptive_analysis(df):
    print("--- Descriptive Analytics ---")

    # Average GPA by Study Group
    summary = df.groupby('Study_Group')['GPA'].mean()
    print("Average GPA by Study Group Type:")
    print(summary)

    # Overall Attendance
    avg_attendance = df['Attendance_Rate'].mean()
    print(f"\nOverall Class Attendance Rate: {avg_attendance:.1%}")

    # Top Performer
    top_performer = df.loc[df['GPA'].idxmax()]
    print(f"Top Performer: {top_performer['Student_Name']} with a GPA of {top_performer['GPA']}\n")


# 2. DIAGNOSTIC ANALYTICS: "Why Did it Happen?"
def diagnostic_analysis(df):
    print("--- Diagnostic Analytics ---")

    # Correlation
    correlation = df['GPA'].corr(df['Study_Hours_Weekly'])
    print(f"Correlation between Weekly Study Hours and GPA: {correlation:.2f}")

    # Regression Model
    X = df[['Study_Hours_Weekly', 'Attendance_Rate', 'Previous_Exam_Score']]
    y = df['GPA']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    print("\nRoot Cause Analysis (Factors impacting Student Success):")
    print(model.params)
    print("\n")


# 3. PREDICTIVE ANALYTICS: "What Will Happen?"
def predictive_analysis(df):
    print("--- Predictive Analytics ---")

    # Train Model
    X = df[['Study_Hours_Weekly', 'Previous_Exam_Score']].values
    y = df['Final_Exam_Projection'].values
    model = LinearRegression().fit(X, y)

    # Predict Sample Student
    sample_student = np.array([[15, 75]])
    forecast = model.predict(sample_student)[0]
    print(f"Projected Final Exam Score for Sample Student: {forecast:.2f}/100")

    # Risk Assessment
    at_risk_count = len(df[df['Attendance_Rate'] < 0.75])
    print(f"Risk Assessment: {at_risk_count} students at risk of failure due to low attendance.\n")


# 4. PRESCRIPTIVE ANALYTICS: "What Should We Do?"
def prescriptive_action():
    print("--- Prescriptive Analytics ---")

    prob = LpProblem("Optimize_Tutoring_Allocation", LpMaximize)
    Math_Hours = LpVariable("Math_Tutoring_Hours", lowBound=0, cat='Continuous')
    Science_Hours = LpVariable("Science_Tutoring_Hours", lowBound=0, cat='Continuous')

    # Objective Function
    prob += 5 * Math_Hours + 4 * Science_Hours

    # Constraints
    prob += Math_Hours + Science_Hours <= 40
    prob += 20 * Math_Hours + 15 * Science_Hours <= 700

    prob.solve()

    print(
        f"Optimal Strategy: Allocate {Math_Hours.varValue:.1f} hours to Math and "
        f"{Science_Hours.varValue:.1f} "
        f"hours to Science."
    )
    print(f"Maximum Expected Grade Gain: {prob.objective.value():.1f} points\n")


# MAIN PROGRAM
if __name__ == "__main__":

    # Mock Student Dataset
    data = {
        'Student_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Study_Group': ['Peer', 'Independent', 'Peer', 'Tutor-Led', 'Independent'],
        'GPA': [3.8, 2.9, 3.5, 3.2, 3.9],
        'Study_Hours_Weekly': [12, 5, 10, 8, 15],
        'Attendance_Rate': [0.95, 0.70, 0.88, 0.80, 0.98],
        'Previous_Exam_Score': [85, 65, 78, 70, 92],
        'Final_Exam_Projection': [88, 68, 80, 75, 95]
    }

    df = pd.DataFrame(data)

    descriptive_analysis(df)
    diagnostic_analysis(df)
    predictive_analysis(df)
    prescriptive_action()