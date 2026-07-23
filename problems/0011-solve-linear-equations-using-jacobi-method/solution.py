import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x=np.zeros_like(b, dtype=float)
	for i in range(n):
		x_old=x.copy()
		for j in range(len(x)):
			off_diagonal_sum=sum(np.delete(A[j], j)*np.delete(x_old, j))
			x[j]=(1/A[j][j])*(b[j]-off_diagonal_sum)
	x=np.round(x, decimals=4)
	return x.tolist()