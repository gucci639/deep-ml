import numpy as np
import math

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	x, y, z = 0, 0, 0
	for i in range(len(point)):
		if i == 0:
			x = point[i]
		elif i == 1:
			y = point[i]
		elif i == 2:
			z = point[i]
	
	derivatives = {
		'poly2d': (2*x*y + y**2, x**2 + 2*x*y),
		'exp_sum': (math.exp(x+y), math.exp(x+y)),
		'product_sin': (math.sin(y), x*math.cos(y)),
		'poly3d': (2*x*y, x**2 + z**2, 2*y*z),
		'squared_error': (2*(x-y), -2*(x-y))
	}
	return derivatives[func_name]
