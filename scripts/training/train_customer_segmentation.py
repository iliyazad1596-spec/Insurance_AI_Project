# ==========================================================
# CUSTOMER SEGMENTATION USING K-MEANS
# ==========================================================

import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 60)
print("Loading Customer Dataset...")
print("=" * 60)

df = pd.read_csv("data/processed/customer_processed.csv")

print(df.head())

# ==========================================================
# FEATURE SCALING
# ==========================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(df)

os.makedirs("models", exist_ok=True)

joblib.dump(
    scaler,
    "models/customer_scaler.pkl"
)

# ==========================================================
# ELBOW METHOD
# ==========================================================

print("\nCalculating Elbow Method...")

wcss = []

for i in range(2, 11):

    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    wcss.append(model.inertia_)

os.makedirs("reports", exist_ok=True)

plt.figure(figsize=(8,5))

plt.plot(
    range(2,11),
    wcss,
    marker="o"
)

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.title("Elbow Method")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "reports/customer_elbow_method.png"
)

plt.close()

# ==========================================================
# FINAL MODEL
# ==========================================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

# ==========================================================
# SILHOUETTE SCORE
# ==========================================================

score = silhouette_score(
    X_scaled,
    clusters
)

print("\nSilhouette Score :", round(score,4))

# ==========================================================
# PCA VISUALIZATION
# ==========================================================

pca = PCA(n_components=2)

pca_features = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))

plt.scatter(
    pca_features[:,0],
    pca_features[:,1],
    c=clusters
)

plt.title("Customer Segments")

plt.xlabel("PCA 1")

plt.ylabel("PCA 2")

plt.tight_layout()

plt.savefig(
    "reports/customer_clusters.png"
)

plt.close()

# ==========================================================
# CLUSTER SUMMARY
# ==========================================================

summary = df.groupby("Cluster").mean()

summary.to_csv(
    "reports/customer_cluster_summary.csv"
)

# ==========================================================
# SAVE MODEL
# ==========================================================

joblib.dump(
    kmeans,
    "models/customer_segmentation_model.pkl"
)

df.to_csv(
    "data/processed/customer_segmented.csv",
    index=False
)

print("\n")
print("=" * 60)
print("CUSTOMER SEGMENTATION COMPLETED")
print("=" * 60)

print("\nFiles Created")

print("models/customer_segmentation_model.pkl")

print("models/customer_scaler.pkl")

print("reports/customer_elbow_method.png")

print("reports/customer_clusters.png")

print("reports/customer_cluster_summary.csv")

print("data/processed/customer_segmented.csv")