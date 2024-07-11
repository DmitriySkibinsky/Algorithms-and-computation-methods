# Introduction to Numerical Integration

<p>&nbsp;&nbsp;&nbsp;&nbsp;Numerical integration is a fundamental technique in computational mathematics used to approximate the integral of a function when an analytical solution is difficult or impossible to obtain. This article explores several sophisticated methods for numerical integration, focusing on their application to matrix solutions. We will delve into:

<p>&nbsp;&nbsp;&nbsp;&nbsp;Simpson's Method with Error Control via the Runge Formula: Simpson's method is a widely used approach for numerical integration that approximates the integral of a function using quadratic polynomials. By implementing error control through the Runge formula, this method enhances the accuracy of the integration, making it more reliable for complex computations.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Gauss-Kronrod, Chebyshev, or Monte Carlo Methods: These advanced techniques offer different strategies for improving the precision of numerical integration. The Gauss-Kronrod method extends Gaussian quadrature rules to provide an estimate of the error, while the Chebyshev method uses orthogonal polynomials to achieve high accuracy. The Monte Carlo method, on the other hand, employs probabilistic sampling to estimate integrals, making it particularly useful for high-dimensional problems.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Adaptive Methods Using Simpson's or Gauss's Methods: Adaptive integration techniques adjust the step size dynamically to meet a desired accuracy level. By combining Simpson's or Gauss's methods with an adaptive strategy, these techniques optimize computational resources while ensuring precise results.

<p>&nbsp;&nbsp;&nbsp;&nbsp;In this article, we will discuss the theoretical foundations of these methods, their implementation details, and their practical applications in solving complex matrix problems. Through detailed examples and comparisons, we aim to provide a comprehensive understanding of these numerical integration techniques and their effectiveness in various computational scenarios.


# Monte Carlo Integration Algorithm
<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/monte-carlo.jpg" alt="monte-carlo">
</p>

  
<p>&nbsp;&nbsp;&nbsp;&nbsp;The Monte Carlo algorithm is a numerical method that uses random sampling to estimate the values of integrals. In general, this method involves the following steps. First, the function 𝑓(𝑥) to be integrated over a given interval [𝑎,𝑏] is defined. Then, a probability density function (PDF) is chosen to describe how random points are distributed over this interval. For simplicity, a uniform distribution is often used. Next, a large number of random points 𝑥𝑖 are generated within the given interval according to the chosen PDF. These points are used to compute the values of the function 𝑓(𝑥𝑖). The PDF values at these points 𝑝(𝑥𝑖) are also computed. The final estimate of the integral is obtained by averaging the ratio 𝑓(𝑥𝑖)/𝑝(𝑥𝑖) for all generated random points.

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/example1.png" alt="example1">
</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;For generating random points, we use a uniform distribution over the interval from 0 to 3, where the PDF is: 𝑝(𝑥) = 1/3 for 0 ≤ 𝑥 ≤ 3. Also we find the maximum value of the function along the y axis - 0.(1). Therefore, we can set the random point generation edge along the y axis to 0.12

<p>&nbsp;&nbsp;&nbsp;&nbsp;Next, a specified number of random points 𝑥𝑖 are generated within the interval from 0 to 3. These points are uniformly distributed, meaning each point has an equal probability of being selected. Then, the values of the function 𝑓(𝑥𝑖) are computed for all generated random points. Since we are using a uniform distribution, the PDF values for all points 𝑥𝑖 are equal to 1/3

<p>&nbsp;&nbsp;&nbsp;&nbsp;The final estimate of the integral is obtained by averaging the ratio 𝑓(𝑥𝑖)/𝑝(𝑥𝑖) for all random points. This ratio accounts for the probability of each value, leading to an accurate estimate of the integral.

```python
import math
import random
import time

def monte_carlo():
    n = 100000
    count = 0

    # Initialize the random number generator only once
    random.seed(time.time())

    for _ in range(n):
        # Generate a random number from 0 to 3
        random_x = random.uniform(0, 3.0)
        # Generate a random number from 0 to 0.12
        random_y = random.uniform(0, 0.12)

        if random_y < (math.sin(random_x)**2) / (13 - 12 * math.cos(random_x)):
            count += 1

    # Calculate the area
    area = count / n * 3.0 * 0.12

    return area

def main():
    k = 20
    sumS1 = 0.0
    sumS2 = 0.0

    for _ in range(k):
        a = monte_carlo()
        print(f"{a:.5f}")
        sumS1 += a
        sumS2 += a**2

    sumS2 /= k
    sumS1 = (sumS1 / k)**2

    sigma = math.sqrt(sumS2 - sumS1)
    print(f"Sigma: {sigma:.5f}")

if __name__ == "__main__":
    main()
```

### Advantages
<p>&nbsp;&nbsp;&nbsp;&nbsp;Versatility: Monte Carlo integration is extremely versatile and can be applied to a wide range of problems. It does not require the function to be smooth or continuous, making it suitable for integrating complex functions with discontinuities or sharp peaks.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Dimensionality: One of the most significant advantages is that it works in any 𝑛-dimensional space. While traditional numerical integration methods struggle with higher dimensions due to the curse of dimensionality, Monte Carlo methods remain relatively efficient as the number of dimensions increases.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Ease of Implementation: The algorithm is straightforward to implement. It primarily involves generating random points and averaging the function values, which can be done with simple programming constructs.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Statistical Interpretation: The results from Monte Carlo integration come with a natural statistical interpretation, providing a clear measure of the uncertainty and error associated with the estimate.

### Disadvantages
<p>&nbsp;&nbsp;&nbsp;&nbsp;Convergence Rate: The convergence rate of Monte Carlo integration is relatively slow compared to some deterministic methods. The error decreases as 1/sqrt(N), where 𝑁 is the number of samples, which means that to reduce the error by a factor of 10, the number of samples must be increased by a factor of 100.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Computational Cost: Because of the slow convergence rate, achieving high precision requires a large number of samples, which can be computationally expensive. This is particularly relevant when the function evaluations are costly.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Randomness Quality: The quality of the random number generator can affect the accuracy and reliability of the results. Poor-quality random number generators can introduce biases and reduce the effectiveness of the method.
<p>&nbsp;&nbsp;&nbsp;&nbsp;Complexity in High Precision: While Monte Carlo methods are efficient in higher dimensions, obtaining very high precision can still be challenging and resource-intensive, as the number of samples required for a given precision increases exponentially.

## Simpson's Method
<p>&nbsp;&nbsp;&nbsp;&nbsp;Simpson's method, also known as Simpson's rule, is a numerical technique for approximating the definite integral of a function. It is particularly useful when an exact analytical solution to the integral is difficult or impossible to obtain. The method is based on approximating the integrand using quadratic polynomials.

### How Simpson's Method Works
<p>&nbsp;&nbsp;&nbsp;&nbsp;Simpson's rule works by dividing the interval [𝑎,𝑏] into an even number of subintervals, typically denoted as 𝑛. Each subinterval has a width ℎ = (𝑏−𝑎)/𝑛. For each pair of subintervals, Simpson's rule fits a quadratic polynomial (parabola) through three points: the endpoints of the interval and the midpoint. The definite integral over the interval is then approximated by the integral of this polynomial.

The formula for Simpson's rule for an interval [𝑎,𝑏] divided into 𝑛 subintervals (where 𝑛 is even) is:
<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/main.png" alt="main">
</p>

Where:
𝑥0 = 𝑎
𝑥𝑛 = 𝑏
𝑥𝑖 = 𝑎 + 𝑖 ⋅ ℎ for 𝑖 = 1, 2, …, 𝑛
As a result, we get a situation where the multipliers will alternate 1, 4, 2, 4, 2, ..., 4, 1

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/maxresdefault.jpg" alt="maxresdefault">
</p>

### Steps to Apply Simpson's Rule
1. Divide the Interval: Divide the interval [𝑎,𝑏] into 𝑛 subintervals of equal width ℎ. Ensure 𝑛 is even.
2. Evaluate the Function: Compute the function values at the endpoints and midpoints of the subintervals.
3. Apply the Formula: Use the Simpson's rule formula to approximate the integral.

Example:
Consider the function 

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/form.png" alt="form">
</p>

Over the interval [0,3]. To approximate the integral using Simpson's rule with 𝑛 = 1000:

``` python
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


```

### Advantages of Simpson's Method

<b>High Accuracy<b/>:
- Polynomial Approximation. By using quadratic polynomials (parabolas) to approximate the integrand, Simpson's rule typically provides a higher accuracy compared to methods that use linear approximations, like the trapezoidal rule.
- Error Reduction: The error in Simpson's rule decreases faster as the number of subintervals increases, specifically, the error is proportional to 1/𝑛^4 for smooth functions.

<b>Simplicity<b/>:
- Easy to Implement: The algorithm is straightforward to implement programmatically. The process involves simple arithmetic operations and can be easily coded.
- Efficiency: It provides a good balance between computational efficiency and accuracy. With a moderate number of subintervals, it often achieves sufficiently accurate results for many practical problems.

<b>Broad Applicability<b/>:
- Versatility: Simpson's method is applicable to a wide range of integrable functions, including those that are difficult to integrate analytically.
- Composite Simpson's Rule: By applying the rule over multiple subintervals, it can handle integrals over any finite interval.

### Limitations and Downsides of Simpson's Method

<b>Requirement of an Even Number of Subintervals<b/>:
- Fixed Interval Count: The method requires the number of subintervals 𝑛 to be even. This restriction can be inconvenient and may require adjustments to the chosen interval division.
- Additional Complexity: If an odd number of subintervals is desired, modifications or alternative methods must be used, adding complexity to the process.

<b>Dependency on Function Smoothness<b/>:
- Smooth Functions Preferred: Simpson's rule assumes that the function being integrated is sufficiently smooth. If the function has discontinuities or sharp changes, the approximation may not be accurate.
- Oscillatory Functions: For highly oscillatory functions, Simpson's rule might not perform well, and other specialized methods may be needed.

<b>Computational Load<b/>:
- Higher Order Calculations: While more accurate, Simpson's rule involves more function evaluations and arithmetic operations than some simpler methods, which can increase computational time, especially for complex or computationally expensive functions.

