import copy
# import numpy as np

def zero_matrix(x):
    return [0] * x


def max_value(matrix):
    k = matrix[0][0]
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > k:
                k = matrix[i][j]
    return k


def zeidel(a, b, eps=1e-9):
    m = len(b)
    x = zero_matrix(m)
    d = zero_matrix(m)
    iteration = 0
    the_end = False
    while not the_end:
        # y = np.copy(x)
        y = copy.deepcopy(x)
        for i in range(m):
            s1 = sum(A[i][j] * y[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            y[i] = (b[i] - s1 - s2) / A[i][i]
            # d[i] = np.fabs (y[i] - x[i])
            d[i] = abs(y[i] - x[i])
        p = max(d)
        iteration += 1
        x = y
        the_end = p <= eps
        if iteration == 1000: the_end = True
    return x, iteration, p


A = [[2, -1, 0], [0, 5, 2], [15, -1, 3]]
B = [3, 7, 4]

x, it, p = zeidel(A, B)

print('Итерация:', it)
print('X =', x)
print('Погрешность =', p)