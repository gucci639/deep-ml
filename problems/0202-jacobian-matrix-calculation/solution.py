import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Jacobian matrix using numerical differentiation.
    
    Args:
        f: Function that takes a list and returns a list
        x: Point at which to evaluate the Jacobian
        h: Step size for finite differences
    
    Returns:
        Jacobian matrix as list of lists
    """
    # Your code here
    jacobian=[[0.0 for i in range(len(x))] for j in range(len(f(x)))]
    for j in range(len(x)):
        tweak_x=list(x)
        tweak_x[j]+=h
        new_screens = f(tweak_x)
        for i in range(len(f(x))):
            diff = new_screens[i] - f(x)[i]
            deriv = diff / h
            jacobian[i][j] = deriv
    return jacobian
    pass