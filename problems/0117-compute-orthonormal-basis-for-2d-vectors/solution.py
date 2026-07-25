import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    # Your code here
    basis = []
    for i in vectors:
        v=np.array(i)
        v=v-sum([np.dot(v,j)/np.dot(j,j)*j for j in basis])
        if np.linalg.norm(v)>tol:
            v=v/np.linalg.norm(v)
            basis.append(v)
    return basis