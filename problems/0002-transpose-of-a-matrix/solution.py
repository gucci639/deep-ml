def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    new=[[0]*len(a) for _ in range(len(a[-1]))]
    # Your code here
    for i in range(len(a[-1])):
        for j in range(len(a)):
            new[i][j]=a[j][i]
    return new