import math
def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
    """
    Compute the derivative of cross-entropy loss with respect to logits.
    
    Args:
        logits: Raw model outputs (before softmax)
        target: Index of the true class (0-indexed)
        
    Returns:
        Gradient vector where gradient[i] = dL/d(logits[i])
    """
    # Your code here
    softmax_sum = sum(math.exp(i) for i in logits)
    softmax = [math.exp(i) / softmax_sum for i in logits]
    deriv_cel= [softmax[i] - (1 if i == target else 0) for i in range(len(logits))]
    return deriv_cel
