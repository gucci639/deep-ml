def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[-1])!=len(b):
		return -1
	c=[[0 for i in range(len(b[-1]))] for i in range(len(a))]
	for i in range(len(a)):
		for j in range(len(b[-1])):
			c[i][j]=sum(a[i][k]*b[k][j] for k in range(len(b)))
	return c