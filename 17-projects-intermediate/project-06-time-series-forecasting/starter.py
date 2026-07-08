"""
Time Series Forecasting — starter scaffold
Prefer module 15 OR this project — see TIME_SERIES_LEARNING_PATH.md
Dataset: Airline passengers or similar in data/
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/air_passengers.csv")


def load_series(path: Path = DATA_PATH) -> pd.Series:
    if not path.exists():
        raise FileNotFoundError(
            f"Place time series CSV at {path}. Index should be datetime."
        )
    df = pd.read_csv(path, parse_dates=["date"], index_col="date")
    return df.squeeze()


def exploratory_analysis(series: pd.Series) -> None:
    """TODO: Plot series, decomposition, ACF/PACF."""
    print(series.describe())
    print(series.index.min(), "→", series.index.max())


def train_test_split_time(series: pd.Series, test_horizon: int = 12):
    """TODO: Hold out last test_horizon points — no random split."""
    train = series.iloc[:-test_horizon]
    test = series.iloc[-test_horizon:]
    return train, test


def fit_arima(train: pd.Series):
    """TODO: statsmodels ARIMA or pmdarima auto_arima."""
    raise NotImplementedError


def fit_lstm(train: pd.Series):
    """TODO: Optional — sequences with TensorFlow/Keras."""
    raise NotImplementedError


def evaluate_forecast(test: pd.Series, forecast) -> None:
    """TODO: RMSE, MAPE, plot actual vs predicted."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 6: TIME SERIES FORECASTING (starter)")
    print("=" * 60)
    series = load_series()
    exploratory_analysis(series)
    train, test = train_test_split_time(series)
    arima_forecast = fit_arima(train)
    evaluate_forecast(test, arima_forecast)


if __name__ == "__main__":
    main()
