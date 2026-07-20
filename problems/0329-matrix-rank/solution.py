import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    A=A.astype(float).copy()
    m, n = A.shape
    rank=0

    for col in range(n):
        if rank>=min(m,n):
            break
        pivot_row=rank+np.argmax(np.abs(A[rank:, col]))

        if abs(A[pivot_row, col])< tol:
            continue

        A[[rank, pivot_row]]=A[[pivot_row, rank]]

        for row in range(rank+1,m):
            factor=A[row,col]/A[rank,col]
            A[row,col:]-=factor*A[rank,col:]
        rank+=1

    return rank