import numpy as np

def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    eigvals = np.linalg.eigvals(hessian)
    if np.all(eigvals > tol):
        return -1  # минимум
    if np.all(eigvals < -tol):
        return 1   # максимум
    if np.any(eigvals > tol) and np.any(eigvals < -tol):
        return 0   # седловая точка
    return None    # вырожденная или неопределённая