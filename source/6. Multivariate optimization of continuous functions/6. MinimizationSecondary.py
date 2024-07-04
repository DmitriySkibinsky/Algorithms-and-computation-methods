import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def anckley(x):
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))) - np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1]))) + np.e + 20

def anckley_gradient(x):
    frstsq = (-0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2)))
    scndsq = (0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])))
    dx = -20 * frstsq * np.exp(frstsq) * (-0.2) * (0.5 * (x[0] ** 2 + x[1] ** 2)) ** (-1 / 2) * x[0] - scndsq * np.exp(
        scndsq) * 0.5 * 2 * np.pi * (-np.sin(2 * np.pi * x[0]))
    dy = -20 * frstsq * np.exp(frstsq) * (-0.2) * (0.5 * (x[0] ** 2 + x[1] ** 2)) ** (-1 / 2) * x[1] - scndsq * np.exp(
        scndsq) * 0.5 * 2 * np.pi * (-np.sin(2 * np.pi * x[1]))
    return np.array([dx, dy])

def anckley_hessian(x):
    return np.array([
        [32 * x[0]**2 + 8 - 42 + 12 * x[1]**2 + 4 * (x[0] + x[1]), 4 * (x[0] + x[1])],
        [4 * (x[0] + x[1]), 4 * x[0] + 12 * x[1]**2 - 26 + 4 * (x[0] + x[1])]
    ])

def newton_method(f, f_prime, f_double_prime, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        grad = f_prime(x)
        hess_inv = np.linalg.inv(f_double_prime(x))
        delta_x = -np.dot(hess_inv, grad)
        x = x + delta_x
        if np.linalg.norm(delta_x) < tol:
            break
    return x

def plot_himmelblau():
    x = np.linspace(-6, 6, 100)
    y = np.linspace(-6, 6, 100)
    X, Y = np.meshgrid(x, y)
    Z = anckley([X, Y])

    plt.figure(figsize=(8, 6))
    plt.contour(X, Y, Z, levels=np.logspace(0, 5, 35), cmap='viridis', alpha=0.8)
    plt.colorbar(label='log scale')
    plt.xlabel('x')
    plt.ylabel('y')

def main():
    plot_himmelblau()
    starting_points = [
        [-4, -4],
        [-4, 4],
        [4, -4],
        [4, 4]
    ]
    for point in starting_points:
        minimum = newton_method(anckley, anckley_gradient, anckley_hessian, point)
        print(f"Минимум в точке: {minimum}")
        plt.scatter(minimum[0], minimum[1], color='red', marker='o')
    plt.show()

if __name__ == "__main__":
    main()