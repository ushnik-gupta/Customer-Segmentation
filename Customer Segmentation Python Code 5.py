import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer Segmentation.csv")

plt.figure(figsize=(8,6))

sns.heatmap(

df[

['Age',

'Annual_Income',

'Spending_Score',

'Purchase_Frequency']

]

.corr(),

annot=True

)

plt.title(

'Customer Correlation Heatmap'

)

plt.show()
