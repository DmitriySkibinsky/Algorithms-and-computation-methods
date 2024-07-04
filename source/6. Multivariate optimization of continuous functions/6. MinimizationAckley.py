import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Function to find all local minima of a given function using steepest descent
def find_local_minima(func, grad_func, initial_points, learning_rate=0.01, tolerance=1e-6, max_iterations=10000):
    min_points = set()  # use a set to store unique minimum points
    for initial_point in initial_points:
        current_point = np.array(initial_point)
        iterations = 0

        while iterations < max_iterations:
            gradient = grad_func(*current_point)
            if np.linalg.norm(gradient) < tolerance:
                min_points.add(tuple(np.round(current_point, decimals=6)))  # add the minimum point to the set
                break

            # Determine the step size along the anti-gradient direction
            step_size = dichotomy_search(func, current_point, gradient)

            # Move along the anti-gradient direction with the chosen step size
            new_point = current_point - learning_rate * step_size * gradient

            # Check if the step size has become too small
            if np.linalg.norm(new_point - current_point) < tolerance:
                min_points.add(tuple(np.round(current_point, decimals=6)))  # add the minimum point to the set
                break

            current_point = new_point
            iterations += 1

    return list(min_points)

# Dichotomy method to find the optimal step size
def dichotomy_search(func, current_point, gradient, tol=1e-6):
    # Define the function to minimize
    def line_search_function(alpha):
        return func(*(current_point - alpha * gradient))

    # Initial values
    a, b = 0, 1
    delta = tol / 10

    # Iterative process to find the optimal step size
    while (b - a) > tol:
        # Choose two intermediate points
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta

        # Evaluate the function values at the chosen points
        f1 = line_search_function(x1)
        f2 = line_search_function(x2)

        # Update the interval
        if f1 < f2:
            b = x2
        else:
            a = x1

    return (a + b) / 2

# Define the Ackley function for demonstration
def ackley(x, y):
     return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

# Define the gradient of the function
def ackley_gradient(x, y):
    frstsq = (-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2)))
    scndsq = (0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))
    dx = -20 * frstsq * np.exp(frstsq) * (-0.2) * (0.5 * (x ** 2 + y ** 2)) ** (-1/2) * x - scndsq * np.exp(scndsq) * 0.5 * 2 * np.pi * (-np.sin(2*np.pi*x))
    dy = -20 * frstsq * np.exp(frstsq) * (-0.2) * (0.5 * (x ** 2 + y ** 2)) ** (-1/2) * y - scndsq * np.exp(scndsq) * 0.5 * 2 * np.pi * (-np.sin(2*np.pi*y))
    return np.array([dx, dy])

# Initial points to start steepest descent
initial_points = [(x, y) for x in np.linspace(-10, 10, 10) for y in np.linspace(-10, 10, 10) if not (x == 0 and y == 0)]
print(initial_points)

# Find all local minima of the Ackley function using steepest descent
min_points = find_local_minima(ackley, ackley_gradient, initial_points)

print("Found local minima:", min_points)

# Plotting the function
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=np.logspace(0, 5, 35))
plt.scatter(*zip(*min_points), color='red', label='Local Minima')
plt.scatter([0], [0], color='blue', label='Global Minimum')

# Displaying the legend
plt.legend()
plt.title('Minima of the Ackley Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
