import math

# Function to be integrated
def f(x):
    return (math.sin(x)**2)/(13-12*math.cos(x))

# Adaptive Simpson's method for calculating the integral
def adaptive_simpson(a, b, epsilon):
    # Calculate the value using Simpson's method for the entire interval [a, b]
    simpson_full = simpson(a, b)

    # Divide the interval [a, b] into two subintervals and calculate the values using Simpson's method on each
    mid = (a + b) / 2
    simpson_left = simpson(a, mid)
    simpson_right = simpson(mid, b)

    # Calculate the difference between the original value and the sum of values on the subintervals
    diff = simpson_left + simpson_right - simpson_full

    # If the difference is less than epsilon, return the sum of the values on the subintervals
    if abs(diff) < epsilon:
        return simpson_left + simpson_right

    # Otherwise, recursively apply the adaptive method to each subinterval
    left_result = adaptive_simpson(a, mid, epsilon/2)
    right_result = adaptive_simpson(mid, b, epsilon/2)

    # Return the sum of the values on the subintervals
    return left_result + right_result

# Simpson's method for calculating the integral on the interval [a, b]
def simpson(a, b):
    h = (b - a) / 2
    x0 = f(a)
    x1 = f((a + b) / 2)
    x2 = f(b)
    integral = (h / 3) * (x0 + 4 * x1 + x2)
    return integral

# Given parameters: integration limits and error tolerance
a = 0
b = 6
epsilon = 1e-3

# Solve using the adaptive Simpson's method
result = adaptive_simpson(a, b, epsilon)

# Print the integral value
print("Integral value (adaptive Simpson's method):", result)
