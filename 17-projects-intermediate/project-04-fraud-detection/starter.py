"""
Credit Card Fraud Detection — starter scaffold
Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
Place creditcard.csv in data/
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


DATA_PATH = Path("data/creditcard.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Download creditcard.csv to {path}")
    return pd.read_csv(path)


def explore(df: pd.DataFrame) -> None:
    """TODO: Class imbalance ratio, amount distribution."""
    print("Fraud rate:", df["Class"].mean())
    print(df["Amount"].describe())


def preprocess(df: pd.DataFrame):
    """TODO: Scale Amount/Time; return features and labels."""
    X = df.drop(columns=["Class"])
    y = df["Class"]
    return X, y


def train_with_imbalance(X_train, y_train):
    """TODO: class_weight, SMOTE, or isolation forest baseline."""
    raise NotImplementedError


def evaluate(model, X_test, y_test):
    """TODO: Precision-recall curve, PR-AUC, cost-sensitive metrics."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 4: FRAUD DETECTION (starter)")
    print("=" * 60)
    df = load_data()
    explore(df)
    X, y = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = train_with_imbalance(X_train, y_train)
    evaluate(model, X_test, y_test)


if __name__ == "__main__":
    main()
