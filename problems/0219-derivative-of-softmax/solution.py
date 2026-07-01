import math

def softmax_derivative(x: list[float]) -> list[list[float]]:
    """
    Compute the Jacobian matrix of the softmax function.
    
    Args:
        x: Input vector of real numbers
        
    Returns:
        Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
    """
    # Your code here
    softmax=[math.exp(i)/sum(math.exp(j) for j in x) for i in x]
    jacobian=[[0.0 for _ in x] for _ in x]
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                jacobian[i][j] = softmax[i]*(1-softmax[j])
            else:
                jacobian[i][j] = -softmax[i]*softmax[j]
    return jacobian