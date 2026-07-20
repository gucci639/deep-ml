from math import sqrt
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    trace=matrix[0][0]+matrix[1][1]
    d=trace**2-4*det
    eigenvalues=[(trace+sqrt(d))/2, (trace-sqrt(d))/2]
    return eigenvalues