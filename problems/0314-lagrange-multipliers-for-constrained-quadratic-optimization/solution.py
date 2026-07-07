import numpy as np

def lagrange_optimize(Q: np.ndarray, c: np.ndarray, a: np.ndarray, b: float) -> dict:
    """
    Solve constrained quadratic optimization using Lagrange multipliers.
    
    Minimize: f(x) = (1/2) x^T Q x + c^T x
    Subject to: a^T x = b
    
    Args:
        Q: 2x2 symmetric positive definite matrix
        c: 2-element vector (linear coefficients)
        a: 2-element vector (constraint coefficients)
        b: scalar (constraint value)
    
    Returns:
        Dictionary with 'x', 'lambda', and 'objective' keys
    """
    kkt=np.zeros((3,3))
    kkt[0:2,0:2]=Q
    kkt[0:2,2]=-a
    kkt[2,0:2]=a.T
    rhs=np.zeros(3)
    rhs[0:2]=-c
    rhs[2]=b
    solution=np.linalg.solve(kkt,rhs)
    x=solution[0:2]
    lambda_=solution[2]
    objective=(1/2)*x.T@Q@x+c.T@x
    return {
        'x': [round(float(i),4) for i in x],
        'lambda': round(float(lambda_),4),
        'objective': round(float(objective),4)
    }
