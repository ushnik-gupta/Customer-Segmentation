import pandas as pd

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer Segmentation.csv")

print(df.head())

print("\nDataset Shape")

print(df.shape)

print("\nMissing Values")

print(df.isnull().sum())

print("\nAverage Income")

print(df['Annual_Income'].mean())

print("\nHighest Spending Score")

print(df['Spending_Score'].max())

print("\nAverage Purchase Frequency")

print(df['Purchase_Frequency'].mean())

print("\nGender Wise Income")

print(

df.groupby(

'Gender'

)['Annual_Income']

.mean()

)

print("\nGender Wise Spending")

print(

df.groupby(

'Gender'

)['Spending_Score']

.mean()

)

print("\nCorrelation Matrix")

print(

df[

['Age',

'Annual_Income',

'Spending_Score',

'Purchase_Frequency']

]

.corr()

)
