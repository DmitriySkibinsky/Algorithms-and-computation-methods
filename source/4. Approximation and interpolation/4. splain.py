import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

class CubicSpline:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x

    def evaluate(self, x):
        i = 0
        for j in range(1, len(self.x)):
            if x < self.x[j]:
                i = j - 1
                break
        dx = x - self.x[i]
        #print(self.a[-1], self.b[-1], self.c[-1], self.d[-1])
        return self.a[i] + self.b[i]*dx + self.c[i]*dx**2 + self.d[i]*dx**3

def compute_cubic_spline(x, y):
    n = len(x)
    h = [x[i+1] - x[i] for i in range(n-1)]
    alpha = [3*(y[i+1]-y[i])/h[i] - 3*(y[i]-y[i-1])/h[i-1] for i in range(1, n-1)]
    l = [1] + [0]*(n-2)
    mu = [0] + [0]*(n-2)
    z = [0] + [0]*(n-2)
    for i in range(1, n-1):
        l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i-1] - h[i-1]*z[i-1]) / l[i]
    l[-1] = 1
    z[-1] = 0
    c = [0]*n
    b = [0]*(n-1)
    d = [0]*(n-1)
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (y[j+1]-y[j])/h[j] - h[j]*(c[j+1]+2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    cs = CubicSpline(y, b, c, d, x)

    #l3 = -1
    #print(y[l3], b[l3], c[l3], d[l3], z[l3])

    return cs

def draw_interpolation_graph(cs,y):
    x_min, x_max = cs.x[0], cs.x[-1]
    x_values = np.linspace(x_min, x_max, 1000)
    y_values = [cs.evaluate(x) for x in x_values]
    y_values[-1] = y[-1]

    #print(cs.evaluate(x_values[-2]))
    #print(cs.evaluate(x_values[-1]))

    plt.plot(x_values, y_values, label='Cubic Spline')
    plt.scatter(cs.x, cs.a, label='Data Points')
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.savefig('interpolation.png')
    plt.show()

    print()

def main():
    x = [1, 1.04, 1.08, 1.12, 1.16, 1.20]
    y = [2.7183, 2.8292, 2.9447, 3.0649, 3.1899, 3.3201]
    x.append(x[-1]*1.01)
    y.append(y[-1]*1.01)

    cs = compute_cubic_spline(x, y)
    cs.x.pop()
    cs.a.pop()
    print(cs.a)
    draw_interpolation_graph(cs,y)
    y_at_1_05 = cs.evaluate(1.05)
    print(f"The value of y at x = 1.05 is: {y_at_1_05}")
    y_at_1_09 = cs.evaluate(1.09)
    print(f"The value of y at x = 1.09 is: {y_at_1_09}")
    y_at_1_13 = cs.evaluate(1.13)
    print(f"The value of y at x = 1.13 is: {y_at_1_13}")
    y_at_1_15 = cs.evaluate(1.15)
    print(f"The value of y at x = 1.15 is: {y_at_1_15}")
    y_at_1_17 = cs.evaluate(1.17)
    print(f"The value of y at x = 1.08 is: {y_at_1_17}")


if __name__ == "__main__":
    main()