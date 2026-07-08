"""
Customer Segmentation — starter scaffold
Dataset: Mall customers or similar — see README
"""

from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler


DATA_PATH = Path("data/Mall_Customers.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Place segmentation CSV at {path} (see README for Kaggle link)"
        )
    return pd.read_csv(path)


def select_features(df: pd.DataFrame):
    """TODO: Choose numeric columns for clustering."""
    raise NotImplementedError


def find_optimal_k(X_scaled, k_range=range(2, 11)):
    """TODO: Elbow method and/or silhouette scores."""
    raise NotImplementedError


def cluster(X_scaled, n_clusters: int):
    """TODO: KMeans (and optionally hierarchical)."""
    raise NotImplementedError


def interpret_clusters(df: pd.DataFrame, labels):
    """TODO: Profile each cluster; business naming."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 5: CUSTOMER SEGMENTATION (starter)")
    print("=" * 60)
    df = load_data()
    features = select_features(df)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)
    k = find_optimal_k(X_scaled)
    labels = cluster(X_scaled, k)
    interpret_clusters(df, labels)


if __name__ == "__main__":
    main()
