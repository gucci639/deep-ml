import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    m,n = X.shape
    # Your code here
    for i in range(n_epochs):
        if method == 'stochastic':
            for j in range(m):
                pred=X[j]@weights
                error=pred-y[j]
                weights=weights-learning_rate*2*(error*X[j]).T
        elif method == 'mini_batch':
            for j in range(0,m,batch_size):
                pred=X[j:batch_size+j]@weights
                error=pred-y[j:batch_size+j]
                weights=weights-learning_rate*2/batch_size*(error@X[j:batch_size+j]).T
        else:
            pred=X@weights
            error=pred-y
            weights=weights-learning_rate*2/m*(error@X).T
    return weights