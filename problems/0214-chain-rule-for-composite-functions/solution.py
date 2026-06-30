import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	
	funcderiv = {
		'square': (lambda x: 2*x, lambda x: x**2),
		'sin': (lambda x: math.cos(x), lambda x: math.sin(x)),
		'exp': (lambda x: math.exp(x), lambda x: math.exp(x)),
		'log': (lambda x: 1/x, lambda x: math.log(x))
	}
	current_x=x
	sum_deriv=1
	for i in reversed(functions):
		sum_deriv=sum_deriv*funcderiv[i][0](current_x)
		current_x=funcderiv[i][1](current_x)
	return sum_deriv
