import numpy as np

# Variables to store the minimum value of the objective function and corresponding values of x1, x2, and x3
min_f = 10000
min_x1 = 0
min_x2 = 0
min_x3 = 0

# Iterating through all possible values of x1, x2, and x3 that satisfy the constraints
for x1 in np.arange(0, 100, 0.5):
    for x2 in np.arange(0, 100, 0.5):
        for x3 in np.arange(0, 100, 0.5):
            # Checking if the current values of x1, x2, and x3 satisfy the constraint equations
            if x1 + x2 - 2*x3 >= 4 and 3*x1 + x2 - 4*x3 <= 2:
                # Computing the value of the objective function for the current values of x1, x2, and x3
                f = 3*x1 + 2*x2 - 4*x3

                # Updating the minimum values if the current objective function value is less than the current minimum
                if f < min_f:
                    min_f = f
                    min_x1 = x1
                    min_x2 = x2
                    min_x3 = x3

# Outputting the result
print(f"Minimum value of the objective function: {min_f}")
print(f"Values: x1 = {min_x1}, x2 = {min_x2}, x3 = {min_x3}")
