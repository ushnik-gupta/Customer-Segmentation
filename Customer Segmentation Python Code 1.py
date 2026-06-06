import pandas as pd

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer Segmentation.csv")

print(df.head())

print("\nDataset Shape")

print(df.shape)

print("\nAverage Income")

print(df['Annual_Income'].mean())

print("\nHighest Spending Score")

print(df['Spending_Score'].max())

print("\nAverage Purchase Frequency")

print(df['Purchase_Frequency'].mean())
