# =================== 1. Import libraries ===================
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =================== 2. Load dataset ===================
df = pd.read_csv("Mall_Customers.csv")

# Drop CustomerID
df = df.drop('CustomerID', axis=1)

# Use only Annual Income and Spending Score for clustering
X = df.iloc[:, [2, 3]].values

# =================== 3. Feature Scaling ===================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =================== 4. Train KMeans ===================
# Using 5 clusters based on previous analysis
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# =================== 5. Dynamic Input ===================
while True:
    try:
        income = float(input("Enter customer's Annual Income (k$): "))
        score = float(input("Enter customer's Spending Score (1-100): "))
    except ValueError:
        print("Please enter valid numeric values.")
        continue

    # Scale input using the same scaler
    input_scaled = scaler.transform([[income, score]])

    # Predict cluster
    cluster = kmeans.predict(input_scaled)[0]

    cluster_mean = kmeans.cluster_centers_[cluster]
    print(f"\nPredicted Cluster: {cluster + 1}")
    print(f"Cluster Center (scaled features): Income={cluster_mean[0]:.2f}, Score={cluster_mean[1]:.2f}")

    # Cluster insights
    insights = {
        0: "Low Income, High Spending Score - Optional targeting",
        1: "Average Income, Average Spending Score - Offer low-cost options",
        2: "High Income, Low Spending Score - Improve marketing to convert",
        3: "Low Income, Low Spending Score - Not a priority",
        4: "High Income, High Spending Score - Loyal customers, target with new products"
    }
    print(f"Cluster Insight: {insights[cluster]}")

    more = input("\nAdd another customer? (y/n): ").lower()
    if more != 'y':
        break
