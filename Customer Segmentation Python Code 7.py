import pandas as pd

df = pd.read_csv(
    r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer Segmentation.csv"
)

df.to_excel(
    r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer_Segmentation.xlsx",
    index=False
)

print("Excel Export Successful")
