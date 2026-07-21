import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    x=np.zeros(len(b), dtype=float)
    A=np.column_stack((A,b)).astype(float)
    for pivot in range(len(A)-1):
        max_row=pivot+np.argmax(np.abs(A[pivot:, pivot]))
        if max_row != pivot:
            A[[pivot, max_row]]=A[[max_row, pivot]]
        for row in range(pivot+1, len(A)):
            m_pivot=A[row][pivot]/A[pivot][pivot]
            A[row]-=A[pivot]*m_pivot
    for x_n in range(len(x)-1, -1, -1):
        x[x_n]=(A[x_n][-1]-np.dot(A[x_n][x_n+1:-1], x[x_n+1:]))/A[x_n][x_n]
    return x