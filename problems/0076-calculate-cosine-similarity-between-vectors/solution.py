import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here

    norm_prod = np.linalg.norm(v1) * np.linalg.norm(v2)
    
    # Avoid division by zero
    if norm_prod == 0:
        return (np.zeros_like(np.dot(v1, v2), dtype=float))
        
    return (np.dot(v1, v2) / norm_prod)