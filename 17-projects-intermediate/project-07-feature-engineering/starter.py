"""
Feature Engineering Mastery — starter scaffold
Use House Prices, credit default, or attrition dataset in data/
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


DATA_PATH = Path("data/train.csv")
TARGET_COL = "SalePrice"  # TODO: change per dataset


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Place training CSV at {path}")
    return pd.read_csv(path)


def build_preprocessing_pipeline(df: pd.DataFrame):
    """TODO: ColumnTransformer for numeric/categorical columns."""
    raise NotImplementedError


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """TODO: WOE, target encoding, interactions — document leakage risks."""
    raise NotImplementedError


def select_features(X, y):
    """TODO: Mutual info, RFE, or model-based importance."""
    raise NotImplementedError


def train_evaluate(pipeline, X_train, y_train, X_test, y_test):
    """TODO: Fit pipeline end-to-end; report CV and holdout metrics."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 7: FEATURE ENGINEERING (starter)")
    print("=" * 60)
    df = load_data()
    df = engineer_features(df)
    y = df[TARGET_COL]
    X = df.drop(columns=[TARGET_COL])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    pipe = build_preprocessing_pipeline(X_train)
    train_evaluate(pipe, X_train, y_train, X_test, y_test)


if __name__ == "__main__":
    main()
