def mprint(matrix, b):
    for i in range(len(matrix)):
        print(matrix[i], b[i])

def gaussian_elimination(matrix, b):
    n = len(matrix)
    for i in range(n):
        # Find the maximum element in the column
        max_element_index = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_element_index][i]):
                max_element_index = k
        # Swap rows
        matrix[i], matrix[max_element_index] = matrix[max_element_index], matrix[i]
        b[i], b[max_element_index] = b[max_element_index], b[i]

        # Divide the first element of the row by its leading coefficient
        divisor = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= divisor
        b[i] /= divisor

        # Subtract the first row from the others
        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            matrix[j][i] -= factor * matrix[i][i]
            b[j] -= factor * b[i]

    return matrix, b

matrix = [[3, 0, -1],
          [2, -5, 1],
          [2, -2, 6]]
b = [-4, 9, 8]

matrix, b = gaussian_elimination(matrix, b)
mprint(matrix, b)
