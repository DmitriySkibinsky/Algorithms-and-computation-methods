def hermite_spline(x, x0, x1, f0, f1, df0, df1):
    # Compute the parameter t used for interpolation between points x0 and x1
    t = (x - x0) / (x1 - x0)
    # Compute the square of parameter t
    t2 = t * t
    # Compute the cube of parameter t
    t3 = t2 * t
    # Compute the values of the Hermite basis functions
    h00 = 2*t3 - 3*t2 + 1
    h10 = t3 - 2*t2 + t
    h01 = -2*t3 + 3*t2
    h11 = t3 - t2
    # Calculate the value of the Hermite spline using the basis functions and the values of the function and its derivative at points x0 and x1
    return h00*f0 + h10*(x1-x0)*df0 + h01*f1 + h11*(x1-x0)*df1

# Example usage
x = 2.5
x0 = 1.0
x1 = 3.0
f0 = 2.0
f1 = 3.0
df0 = 1.0
df1 = 2.0

result = hermite_spline(x, x0, x1, f0, f1, df0, df1)
print(f"Hermite spline result: {result}")
