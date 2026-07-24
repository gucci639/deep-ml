import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	b=b.copy()
	x_ini = np.zeros_like(b) if x_ini==None else x_ini
	for i in range(n):
		for j in range(len(x_ini)):
			x_ini[j]=(1/A[j][j])*(b[j]-sum(np.delete(arr=(A[j]*x_ini), obj=j)))
	return x_ini