import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    if func_name == 'exp':
        sum=0.0
        for i in range(n_terms):
            sum+=x**i/factorial(i)
        return sum
    if func_name == 'sin':
        sum=0.0
        for i in range(n_terms):
            sum+=((-1)**i)*x**(2*i+1)/factorial(2*i+1)
        return sum
    if func_name == 'cos':
        sum=0.0
        for i in range(n_terms):
            sum+=((-1)**i)*x**(2*i)/factorial(2*i)
        return sum