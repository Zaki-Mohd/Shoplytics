# =================== 1. Import libraries ===================
from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# =================== 2. Load dataset and Train Model ===================
df = pd.read_csv("Mall_Customers.csv")
df = df.drop('CustomerID', axis=1)
X = df.iloc[:, [2, 3]].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# =================== 3. Create Flask App ===================
app = Flask(__name__)

# =================== 4. Define Routes ===================
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/data')
def get_data():
    # Inverse transform the scaled data to get original values for plotting
    X_original = scaler.inverse_transform(X_scaled)
    cluster_centers_original = scaler.inverse_transform(kmeans.cluster_centers_)
    
    return jsonify({
        'customers': X_original.tolist(),
        'labels': kmeans.labels_.tolist(),
        'cluster_centers': cluster_centers_original.tolist()
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    income = float(data['income'])
    score = float(data['score'])

    input_scaled = scaler.transform([[income, score]])
    cluster = kmeans.predict(input_scaled)[0]

    insights = {
        0: "Low Income, High Spending Score - Optional targeting",
        1: "Average Income, Average Spending Score - Offer low-cost options",
        2: "High Income, Low Spending Score - Improve marketing to convert",
        3: "Low Income, Low Spending Score - Not a priority",
        4: "High Income, High Spending Score - Loyal customers, target with new products"
    }

    return jsonify({
        'cluster': int(cluster + 1),
        'insight': insights[cluster]
    })

# =================== 5. Run App ===================
if __name__ == '__main__':
    app.run(debug=True)
