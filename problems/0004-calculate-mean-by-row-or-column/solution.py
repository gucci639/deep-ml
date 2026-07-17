def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        mean = [0.0 for _ in range(len(matrix[-1]))]
        for i in range(len(matrix[-1])):
            mean[i] = sum(matrix[j][i] for j in range(len(matrix))) / len(matrix)
        return mean

    if mode == 'row':
        mean = [0.0 for _ in range(len(matrix))]
        for i in range(len(matrix)):
            mean[i] = sum(matrix[i][j] for j in range(len(matrix[i]))) / len(matrix[i])
        return mean