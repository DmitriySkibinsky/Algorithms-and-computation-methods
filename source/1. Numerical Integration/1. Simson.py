import numpy as np

# Function we want to integrate
def f(x):
    return (np.sin(x) * np.sin(x)) / (13 - 12 * np.cos(x))

# Integration limits
a = 0
b = 3

# Probability density function (PDF) for generating random points
# In this case, we will use a uniform PDF on the interval [a, b]
def pdf(x):
    return np.where((a <= x) & (x <= b), 1 / (b - a), 0)

# Number of random points for the Monte Carlo method
num_samples = 100000

# Generate random points and compute the integral
random_x = np.random.uniform(a, b, num_samples)
f_values = f(random_x)
pdf_values = pdf(random_x)

# Compute the integral estimate
integral_estimate = np.mean(f_values / pdf_values)

# Print the result
print("Approximate value of the integral:", integral_estimate)
