import numpy as np
from typing import Tuple

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    """Return the (feature_index, threshold) that minimises weighted Gini impurity."""
    # ✏️ TODO: implement
    n, d = X.shape
    best_feature=0
    best_threshold=0.0
    best_gini = float("inf")

    for feature in range(d):
        thresholds = np.unique(X[:,feature])
        for threshold in thresholds:
            left = y[X[:,feature] <= threshold]
            right = y[X[:,feature] > threshold]

            if len(left) == 0 or len(right) == 0:
                continue

            p_left = np.mean(left)
            gini_left = 2*p_left*(1-p_left)

            p_right = np.mean(right)
            gini_right = 2*p_right*(1-p_right)

            gini = (len(left)/n*gini_left + len(right)/n*gini_right)

            if gini < best_gini:
                best_gini = gini
                best_feature = feature
                best_threshold = threshold
                
    return best_feature, best_threshold
            