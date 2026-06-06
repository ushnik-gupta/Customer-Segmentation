import os
os.environ["OMP_NUM_THREADS"] = "1"

import pandas as pd
from sklearn.cluster import KMeans

# Read CSV
df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Customer Segmentation.csv")

# Remove missing values
df = df.dropna(subset=['Annual_Income', 'Spending_Score'])

# Features
X = df[['Annual_Income', 'Spending_Score']]

# KMeans
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Fit model
df['Cluster'] = kmeans.fit_predict(X)

print("\nCustomer Segments")
print(df[['Annual_Income', 'Spending_Score', 'Cluster']].head())
