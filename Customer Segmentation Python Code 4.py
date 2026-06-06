import os
os.environ["OMP_NUM_THREADS"] = "1"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_excel(
    r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Excel Customer_Segmentation.xlsx"
)

print(df.head())
print(df.columns)

df = df.dropna(subset=['Annual_Income', 'Spending_Score'])

X = df[['Annual_Income', 'Spending_Score']]

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x='Annual_Income',
    y='Spending_Score',
    hue='Cluster',
    palette='viridis',
    s=80
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend(title="Cluster")
plt.tight_layout()

plt.show()
