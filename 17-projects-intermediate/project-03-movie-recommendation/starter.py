"""
Movie Recommendation System — starter scaffold
Dataset: https://grouplens.org/datasets/movielens/
Place ratings.csv and movies.csv in data/ (e.g. ml-latest-small)
"""

from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")


def load_ratings_and_movies(data_dir: Path = DATA_DIR):
    ratings_path = data_dir / "ratings.csv"
    movies_path = data_dir / "movies.csv"
    if not ratings_path.exists():
        raise FileNotFoundError(
            f"Download MovieLens files to {data_dir}. See README."
        )
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path) if movies_path.exists() else None
    return ratings, movies


def build_user_item_matrix(ratings: pd.DataFrame):
    """TODO: Pivot or sparse matrix for collaborative filtering."""
    raise NotImplementedError


def train_collaborative_filter(matrix):
    """TODO: Item-based or matrix factorization (e.g. surprise, implicit)."""
    raise NotImplementedError


def recommend(user_id: int, model, n=10):
    """TODO: Return top-N movie titles for user."""
    raise NotImplementedError


def evaluate(model, ratings: pd.DataFrame):
    """TODO: RMSE, precision@k, or holdout evaluation."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 3: MOVIE RECOMMENDATION (starter)")
    print("=" * 60)
    ratings, movies = load_ratings_and_movies()
    print(ratings.head())
    matrix = build_user_item_matrix(ratings)
    model = train_collaborative_filter(matrix)
    evaluate(model, ratings)
    # recommend(1, model)


if __name__ == "__main__":
    main()
