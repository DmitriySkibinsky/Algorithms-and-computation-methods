import numpy as np

# Function we want to integrate
def f(x):
    return (np.sin(x) * np.sin(x)) / (13 - 12 * np.cos(x))

# Integration limits
a = 0
b = 3

# Number of subintervals (should be an even number)
n = 1000

# Simpson's method
def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    integral = y[0] + y[-1]
    
    for i in range(1, n, 2):
        integral += 4 * y[i]
    
    for i in range(2, n-1, 2):
        integral += 2 * y[i]
    
    integral *= h / 3
    return integral

# Calculate the integral
integral_value = simpson(f, a, b, n)

# Print the result
print("Approximate value of the integral using Simpson's method:", integral_value)
