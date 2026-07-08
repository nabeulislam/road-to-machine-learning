"""
MNIST Digit Recognition — starter scaffold
Download MNIST via Keras or place files in data/ per README.
"""

from pathlib import Path

import numpy as np
from sklearn.metrics import classification_report


def load_data():
    """TODO: Load MNIST (e.g. keras.datasets.mnist.load_data())."""
    # from tensorflow.keras.datasets import mnist
    # (x_train, y_train), (x_test, y_test) = mnist.load_data()
    raise NotImplementedError("Load MNIST and return train/test arrays")


def preprocess(x_train, y_train, x_test, y_test):
    """TODO: Normalize pixels, reshape for model input."""
    raise NotImplementedError


def build_model(input_shape, num_classes=10):
    """TODO: Build MLP or small CNN with TensorFlow/Keras."""
    raise NotImplementedError


def train_and_evaluate(model, x_train, y_train, x_test, y_test):
    """TODO: Fit model, predict, print classification_report."""
    raise NotImplementedError


def main():
    print("=" * 60)
    print("PROJECT 1: MNIST DIGIT RECOGNITION (starter)")
    print("=" * 60)
    x_train, y_train, x_test, y_test = load_data()
    x_train, y_train, x_test, y_test = preprocess(x_train, y_train, x_test, y_test)
    input_shape = x_train.shape[1:]
    model = build_model(input_shape)
    train_and_evaluate(model, x_train, y_train, x_test, y_test)
    out = Path("results")
    out.mkdir(exist_ok=True)
    print(f"Save plots and model artifacts to {out.resolve()}")


if __name__ == "__main__":
    main()
