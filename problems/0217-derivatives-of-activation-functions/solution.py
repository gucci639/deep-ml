import math
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	return {
        'sigmoid': math.exp(-x) / (1 + math.exp(-x))**2,
        'tanh': 1 - math.tanh(x)**2,
        'relu': 1 if x > 0 else 0
    }