import numpy as np
import math
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    mse_values=[]
    n=len(labels)
    current_weights=initial_weights.copy()
    current_bias = initial_bias
    current_features=features.copy()
    for _ in range(epochs):
        z = np.dot(features, current_weights) + current_bias
        pred = 1 / (1 + np.exp(-z))

        mse = np.mean((pred - labels)**2)
        mse_values.append(round(mse, 4))

        gradient_factor = (2.0 / n) * (pred - labels) * pred * (1-pred)

        dw = np.dot(current_features.T, gradient_factor)
        db = np.sum(gradient_factor)

        current_weights -= learning_rate * dw
        current_bias -= learning_rate * db

    return np.round(current_weights, 4).tolist(), round(current_bias, 4), mse_values 