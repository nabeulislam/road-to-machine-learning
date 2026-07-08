"""
Ensemble Methods Comparison — starter scaffold
Dataset: Titanic, churn, fraud, or house prices in data/
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import (
    AdaBoostClassifier,
    BaggingClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
    StackingClassifier,
    VotingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split


DATA_PATH = Path("data/train.csv")
TARGET_COL = "Survived"  # TODO: adjust per dataset


def load_and_preprocess(path: Path = DATA_PATH):
    if not path.exists():
        raise FileNotFoundError(f"Place labeled CSV at {path}")
    df = pd.read_csv(path)
    # TODO: encoding, imputation, feature selection
    y = df[TARGET_COL]
    X = df.drop(columns=[TARGET_COL])
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


def build_ensembles():
    """TODO: Configure bagging, boosting, voting, stacking estimators."""
    base = LogisticRegression(max_iter=1000)
    return {
        "bagging": BaggingClassifier(estimator=base, n_estimators=10, random_state=42),
        "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "gradient_boosting": GradientBoostingClassifier(random_state=42),
        "ada_boost": AdaBoostClassifier(random_state=42),
        # "xgboost": ...  # optional
        "voting": VotingClassifier(
            estimators=[
                ("lr", LogisticRegression(max_iter=1000)),
                ("rf", RandomForestClassifier(n_estimators=50, random_state=42)),
            ],
            voting="soft",
        ),
        "stacking": StackingClassifier(
            estimators=[
                ("lr", LogisticRegression(max_iter=1000)),
                ("rf", RandomForestClassifier(n_estimators=50, random_state=42)),
            ],
            final_estimator=LogisticRegression(max_iter=1000),
        ),
    }


def compare_models(models, X_train, y_train):
    """TODO: cross_val_score each; table of mean/std metrics."""
    results = {}
    for name, model in models.items():
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
        results[name] = scores.mean()
        print(f"{name}: F1 CV = {scores.mean():.4f} (+/- {scores.std():.4f})")
    return results


def main():
    print("=" * 60)
    print("PROJECT 8: ENSEMBLE COMPARISON (starter)")
    print("=" * 60)
    X_train, X_test, y_train, y_test = load_and_preprocess()
    models = build_ensembles()
    compare_models(models, X_train, y_train)


if __name__ == "__main__":
    main()
