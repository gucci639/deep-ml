def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot=0
	l_norm=0
	for i in range(len(v)):
		dot+=v[i]*L[i]
		l_norm+=L[i]**2
	scalar = dot/l_norm
	return [scalar*L[i] for i in range(len(L))]
