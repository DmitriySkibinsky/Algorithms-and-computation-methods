# Introduction to Numerical Integration

<p>&nbsp;&nbsp;&nbsp;&nbsp;Numerical integration is a fundamental technique in computational mathematics used to approximate the integral of a function when an analytical solution is difficult or impossible to obtain. This article explores several sophisticated methods for numerical integration, focusing on their application to matrix solutions. We will delve into:

<p>&nbsp;&nbsp;&nbsp;&nbsp;Simpson's Method with Error Control via the Runge Formula: Simpson's method is a widely used approach for numerical integration that approximates the integral of a function using quadratic polynomials. By implementing error control through the Runge formula, this method enhances the accuracy of the integration, making it more reliable for complex computations.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Gauss-Kronrod, Chebyshev, or Monte Carlo Methods: These advanced techniques offer different strategies for improving the precision of numerical integration. The Gauss-Kronrod method extends Gaussian quadrature rules to provide an estimate of the error, while the Chebyshev method uses orthogonal polynomials to achieve high accuracy. The Monte Carlo method, on the other hand, employs probabilistic sampling to estimate integrals, making it particularly useful for high-dimensional problems.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Adaptive Methods Using Simpson's or Gauss's Methods: Adaptive integration techniques adjust the step size dynamically to meet a desired accuracy level. By combining Simpson's or Gauss's methods with an adaptive strategy, these techniques optimize computational resources while ensuring precise results.

<p>&nbsp;&nbsp;&nbsp;&nbsp;In this article, we will discuss the theoretical foundations of these methods, their implementation details, and their practical applications in solving complex matrix problems. Through detailed examples and comparisons, we aim to provide a comprehensive understanding of these numerical integration techniques and their effectiveness in various computational scenarios.


## Monte Carlo Integration Algorithm

<p>&nbsp;&nbsp;&nbsp;&nbsp;The Monte Carlo algorithm is a numerical method that uses random sampling to estimate the values of integrals. In general, this method involves the following steps. First, the function 𝑓(𝑥) to be integrated over a given interval [𝑎,𝑏] is defined. Then, a probability density function (PDF) is chosen to describe how random points are distributed over this interval. For simplicity, a uniform distribution is often used. Next, a large number of random points 𝑥𝑖 are generated within the given interval according to the chosen PDF. These points are used to compute the values of the function 𝑓(𝑥𝑖). The PDF values at these points 𝑝(𝑥𝑖) are also computed. The final estimate of the integral is obtained by averaging the ratio 𝑓(𝑥𝑖)/𝑝(𝑥𝑖) for all generated random points.

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/1.%20Numerical%20Integration/img/example1.png" alt="example1">
</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;For generating random points, we use a uniform distribution over the interval from 0 to 3, where the PDF is: 𝑝(𝑥) = 1/3 for 0 ≤ 𝑥 ≤ 3 

<p>&nbsp;&nbsp;&nbsp;&nbsp;Next, a specified number of random points 𝑥𝑖 are generated within the interval from 0 to 3. These points are uniformly distributed, meaning each point has an equal probability of being selected. Then, the values of the function 𝑓(𝑥𝑖) are computed for all generated random points. Since we are using a uniform distribution, the PDF values for all points 𝑥𝑖 are equal to 1/3

<p>&nbsp;&nbsp;&nbsp;&nbsp;The final estimate of the integral is obtained by averaging the ratio 𝑓(𝑥𝑖)/𝑝(𝑥𝑖) for all random points. This ratio accounts for the probability of each value, leading to an accurate estimate of the integral.
