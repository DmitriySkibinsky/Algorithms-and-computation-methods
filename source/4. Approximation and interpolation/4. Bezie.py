import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def lerp(p1, p2, t):
    return [(1 - t) * p1[i] + t * p2[i] for i in range(len(p1))]


def bezier_curve(points, n_points=100):
    n = len(points)
    curve = []

    for t in range(n_points):
        t /= n_points - 1
        temp_points = points.copy()
        for i in range(n - 1):
            temp_points = [lerp(temp_points[j], temp_points[j + 1], t) for j in range(len(temp_points) - 1)]
        curve.append(temp_points[0])

    return curve


# Setpoints
points = [ [1, 2], [2, 5], [3, 3], [4, 2.77], [5, 10]]

# Drawing a Bezier curve
curve = bezier_curve(points)

# Visualization
import matplotlib.pyplot as plt

x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

curve_x = [point[0] for point in curve]
curve_y = [point[1] for point in curve]

plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color='red', label='Control Points')
plt.plot(curve_x, curve_y, color='blue', label='Bezier Curve')
plt.legend()
plt.show()