from typing import Callable

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Hessian matrix of function f at the given point using finite differences.
    
    Args:
        f: A scalar function that takes a list of floats and returns a float
        point: The point at which to compute the Hessian (list of coordinates)
        h: Step size for finite differences (default: 1e-5)
        
    Returns:
        The Hessian matrix as a list of lists (n x n where n = len(point))
    """
    # Your code here
    hessian=[[0.0 for i in range(len(point))] for j in range(len(point))]
    for j in range(len(point)):
        for i in range(len(point)):
            point_tuned_1=list(point)
            point_tuned_2=list(point)
            point_tuned_3=list(point)
            point_tuned_4=list(point)
            
            point_tuned_1[i]=h+point_tuned_1[i]
            point_tuned_1[j]=h+point_tuned_1[j]

            point_tuned_2[i]=h+point_tuned_2[i]
            point_tuned_2[j]=point_tuned_2[j]-h

            point_tuned_3[i]=point_tuned_3[i]-h
            point_tuned_3[j]=h+point_tuned_3[j]

            point_tuned_4[i]=point_tuned_4[i]-h
            point_tuned_4[j]=point_tuned_4[j]-h

            hessian[j][i]=(f(point_tuned_1)-f(point_tuned_2)-f(point_tuned_3)+f(point_tuned_4))/(4*h**2)
    return hessian
    