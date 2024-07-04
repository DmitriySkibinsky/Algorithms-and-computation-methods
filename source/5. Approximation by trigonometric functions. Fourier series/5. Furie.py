import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def f(x):
    return x+1

def SimpsonMethod(a, b, n, f):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)
    return (h / 3) * sum

def FourierSeries(a, b, N, x):
    y = np.zeros_like(x)

    # Fourier series coefficients
    a0 = SimpsonMethod(a, b, 10000, f) / np.pi

    for i in range(1, N + 1):
        bn = SimpsonMethod(a, b, 10000, lambda x: f(x) * np.sin(i * x)) / np.pi
        an = SimpsonMethod(a, b, 10000, lambda x: f(x) * np.cos(i * x)) / np.pi
        y += an * np.cos(i * x) + bn * np.sin(i * x)

    # Adding a0/2 to the beginning of the series
    for i in range(len(y)):
        y[i] += a0 / 2

    return y

def plotFunction(x, y, filename):
    plt.plot(x, y)
    plt.title('Function Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(filename)
    plt.show()

def main():
    a = float(input("Enter the start of the interval a: "))
    b = float(input("Enter the end of the interval b: "))

    while True:
        N = int(input("Enter the number of Fourier series coefficients (-1 to exit): "))

        if N == -1:
            break

        NumOfPoints = 10000  # Increasing the number of points for a more accurate approximation

        h = (b - a) / NumOfPoints
        x = np.linspace(a, b, NumOfPoints)
        y = FourierSeries(a, b, N, x)

        plotFunction(x, y, "plot.png")

if __name__ == "__main__":
    main()
