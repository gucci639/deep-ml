def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    # Your code here
    trace = sum(matrix[i][i] for i in range(len(matrix)))
    def det(a):
        if len(a)==2:
            return a[0][0]*a[1][1]-a[0][1]*a[1][0]
        else:
            summ=0
            for j in range(0,len(a)):
                M=[row[:] for row in a]
                M.pop(0)
                for row in M:
                    row.pop(j)
                summ+=(((-1)**(j))*a[0][j]*det(M))
            return summ
    det1=det(matrix)
    return (det1, trace)