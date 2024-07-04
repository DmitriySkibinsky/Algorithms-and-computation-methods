import math


def remove_similar_roots(roots):
    new_roots = []
    plus_roots = []
    minus_roots = []
    for i, root in enumerate(roots):
        if abs(root) > 0.001:
            new_roots.append(root)

    for i, root in enumerate(new_roots):
        if root > 1:
            plus_roots.append(root)
        else:
            minus_roots.append(root)

    plus_roots = plus_roots[1::2]
    minus_roots = minus_roots[::2]

    # Combine the two arrays
    all_roots = minus_roots + plus_roots

    return all_roots


def f(x):
    # Check that x is not zero or a multiple of π to avoid division by zero
    if x == 0 or math.isclose(x % math.pi, 0, abs_tol=1e-9):
        return float('inf')  # At x = 0 or multiple of π, the function is undefined, return infinity
    else:
        # Check that sin(x) is not zero to avoid division by zero
        if math.isclose(math.sin(x), 0, abs_tol=1e-9):
            return float('inf')  # At sin(x) = 0, the function is undefined, return infinity
        else:
            return x - (math.cos(x) / math.sin(x))


a, b = map(float, input("Enter the interval values: ").split())
eps = 0.001
h = 0.1
pCounter = int((b - a) / h)  # Number of points between a and b

points = [[a + i * h, a + (i + 1) * h] for i in range(pCounter)]

answ = []

for i in range(pCounter):
    a, b = points[i]
    if f(a) * f(b) > 0:
        continue  # If the function does not change sign on the interval, skip this interval

    while (b - a) > eps:
        c = (a + b) / 2
        if math.isclose(f(c), 0, abs_tol=eps):
            answ.append(c)
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    # Add the found root to the list with the given precision
    answ.append((a + b) / 2)

unique_roots = remove_similar_roots(answ)
print("Equation roots: ", end="")
for root in unique_roots:
    print(root, end=" ")
