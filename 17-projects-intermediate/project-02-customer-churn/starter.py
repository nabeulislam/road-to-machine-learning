"""
Customer Churn Prediction — starter scaffold
Dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Place WA_Fn-UseC_-Telco-Customer-Churn.csv in data/
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


DATA_PATH = Path("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Download Telco churn CSV to {path}. See README for Kaggle link."
        )
    return pd.read_csv(path)


def explore(df: pd.DataFrame) -> None:
    """TODO: Churn rate, missing values, feature distributions."""
    print(df.shape)
    print(df["Churn"].value_counts(normalize=True))


def preprocess(df: pd.DataFrame):
    """TODO: Encode categoricals, scale numerics, return X, y."""
    raise NotImplementedError


def handle_imbalance(X_train, y_train):
    """TODO: SMOTE, class weights, or threshold tuning."""
    return X_train, y_train


def train_models(X_train, y_train):
    """TODO: LogisticRegression, RandomForest, XGBoost with CV."""
    raise NotImplementedError


def evaluate(models, X_test, y_test):
    """TODO: Recall-focused metrics; business cost discussion."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 2: CUSTOMER CHURN (starter)")
    print("=" * 60)
    df = load_data()
    explore(df)
    X, y = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    X_train, y_train = handle_imbalance(X_train, y_train)
    models = train_models(X_train, y_train)
    evaluate(models, X_test, y_test)


if __name__ == "__main__":
    main()
