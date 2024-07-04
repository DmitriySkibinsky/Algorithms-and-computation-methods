import math

def remove_similar_roots(roots):
    new_roots = []
    plus_roots = []
    minus_roots = []
    for i, root in enumerate(roots):
        if abs(root) > 0.001:
            new_roots.append(root)

    for i, root in enumerate(new_roots):
        if root > 0:
            plus_roots.append(root)
        else:
            minus_roots.append(root)

    plus_roots = plus_roots[::2]
    minus_roots = minus_roots[::2]

    # Combine the two arrays
    all_roots = minus_roots + plus_roots

    return all_roots

def f(x):
    if math.isclose(math.sin(x), 0, abs_tol=1e-9):
        return float('nan')  # Return NaN for the cases where sin(x) is close to zero
    else:
        return x - (math.cos(x) / math.sin(x))


def df(x):
    if math.isclose(math.sin(x), 0, abs_tol=1e-9):
        return float('nan')  # Return NaN for the cases where sin(x) is close to zero
    else:
        return 1 + (1 / (math.sin(x)) ** 2)


def find_roots(a, b, eps):
    roots = []
    step = 0.001  # Increased step for checking the sign of the function
    x = a

    while x < b:
        # Check if the function changes sign within the step
        if x + step <= b and f(x) * f(x + step) < 0:
            # The sign of the function changes in this interval, attempt to find a root
            x0 = x + step / 2  # Initial approximation for Newton's method
            delta = eps + 1
            while abs(delta) >= eps:
                x1 = x0 - f(x0) / df(x0)
                delta = x1 - x0
                x0 = x1
            # Check if the root is not too close to any existing root
            if not any(math.isclose(root, x1, abs_tol=eps) for root in roots):
                roots.append(x1)
        x += step
    return roots


a = float(input("Enter the coordinate A of the interval: "))
b = float(input("Enter the coordinate B of the interval: "))
eps = float(input("Enter the precision value: "))

roots = find_roots(a, b, eps)
unique_roots = remove_similar_roots(roots)
print("Found roots:", unique_roots)
