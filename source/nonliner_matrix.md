## Introduction to the Solution of NonLinear Equations

<p>&nbsp;&nbsp;&nbsp;&nbsp;Nonlinear equations play a crucial role in various scientific and engineering disciplines, where the relationships between variables are often complex and cannot be described by simple linear models. These equations arise in a wide range of applications, from physics and chemistry to economics and biology, and solving them is essential for modeling, prediction, and optimization in these fields. However, finding the solutions to nonlinear equations can be challenging due to the absence of general analytic methods, requiring the use of numerical techniques.

<p>&nbsp;&nbsp;&nbsp;&nbsp;In this context, several methods have been developed to approximate the roots of nonlinear equations, each with its own advantages and limitations. Among the most commonly used techniques are the Bisection Method (also known as the Method of Dichotomy), Newton's Method, and the Newton-Raphson Method.

<p>&nbsp;&nbsp;&nbsp;&nbsp;The Bisection Method is a simple yet powerful technique that guarantees convergence by repeatedly dividing the interval where the root lies and narrowing it down until the solution is sufficiently accurate. This method is particularly useful when an initial guess of the solution is not available, or when the function behaves well over a certain interval.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Newton's Method, on the other hand, is an iterative approach that uses the derivative of the function to rapidly converge to a solution. It is known for its efficiency and fast convergence, especially when the initial guess is close to the actual root. However, its performance depends on the nature of the function and the choice of the initial guess, making it less robust in some cases.

<p>&nbsp;&nbsp;&nbsp;&nbsp;The Newton-Raphson Method is a specific application of Newton's Method, particularly useful for solving equations with multiple variables. By extending the principles of Newton's Method to systems of nonlinear equations, the Newton-Raphson Method offers a powerful tool for finding solutions in more complex scenarios. This method is widely used in engineering and scientific computations, where systems of nonlinear equations frequently occur.

<p>&nbsp;&nbsp;&nbsp;&nbsp;In this discussion, we will delve into each of these methods, examining their theoretical foundations, practical implementation, and the scenarios where they excel. By understanding the strengths and limitations of the Bisection Method, Newton's Method, and the Newton-Raphson Method, we can make informed choices about which technique to apply to specific types of nonlinear equations, ultimately improving the efficiency and accuracy of our solutions.

## The dichotomy methods

<p>&nbsp;&nbsp;&nbsp;&nbsp;The bisection method, also known as the method of dichotomy or the interval halving method, is one of the simplest and most reliable numerical techniques for solving nonlinear equations. This method is used to find the root of a continuous function 𝑓(𝑥), meaning the value of 𝑥 for which 𝑓(𝑥) = 0.

### Key Principles of the Method

<p>&nbsp;&nbsp;&nbsp;&nbsp;The bisection method is based on the following fundamental principle: if a function 𝑓(𝑥) is continuous on the interval [𝑎,𝑏] and 𝑓(𝑎) and 𝑓(𝑏) have opposite signs, then there is at least one root within this interval, meaning a value 𝑥 for which 𝑓(𝑥) = 0. This fact follows from the Bolzano-Cauchy theorem.

### Steps of the Method
The bisection method is implemented in several steps:

1. Selecting the Initial Interval: Choose an initial interval [𝑎,𝑏], where 𝑓(𝑎) and 𝑓(𝑏) have opposite signs ( e.g.,  𝑓(𝑎) < 0 and 𝑓(𝑏) > 0 ).

2. Finding the Midpoint of the Interval: Calculate the midpoint of the interval 𝑐 = (𝑎 + 𝑏) / 2.

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/dictotomii.png" alt="dictotomii"
</p>

3. Checking the Sign of the Function at 𝑐:
- If 𝑓(𝑐) = 0, then 𝑐 is the root of the equation, and the process can be terminated.
- If 𝑓(𝑐) ≠ 0, determine on which subinterval [𝑎,𝑐] or [𝑐,𝑏] the function changes sign, and choose this interval as the new interval for the next iteration.

4. Narrowing the Interval: Depending on the sign of 𝑓(𝑐), the interval is halved, and the process is repeated until the interval length becomes sufficiently small or the function value at the midpoint is close enough to zero with the desired accuracy.

```python
import math

def remove_similar_roots(roots):
    new_roots = []
    plus_roots = []
    minus_roots = []
    for i, root in enumerate(roots):
        if abs(root) > 0.001:
            new_roots.append(root)

    for i, root in enumerate(new_roots):
        if root > 1:
            plus_roots.append(root)
        else:
            minus_roots.append(root)

    plus_roots = plus_roots[1::2]
    minus_roots = minus_roots[::2]

    # Combine the two arrays
    all_roots = minus_roots + plus_roots

    return all_roots


def f(x):
    # Check that x is not zero or a multiple of π to avoid division by zero
    if x == 0 or math.isclose(x % math.pi, 0, abs_tol=1e-9):
        return float('inf')  # At x = 0 or multiple of π, the function is undefined, return infinity
    else:
        # Check that sin(x) is not zero to avoid division by zero
        if math.isclose(math.sin(x), 0, abs_tol=1e-9):
            return float('inf')  # At sin(x) = 0, the function is undefined, return infinity
        else:
            return x - (math.cos(x) / math.sin(x))


a, b = map(float, input("Enter the interval values: ").split())
eps = 0.001
h = 0.1
pCounter = int((b - a) / h)  # Number of points between a and b

points = [[a + i * h, a + (i + 1) * h] for i in range(pCounter)]

answ = []

for i in range(pCounter):
    a, b = points[i]
    if f(a) * f(b) > 0:
        continue  # If the function does not change sign on the interval, skip this interval

    while (b - a) > eps:
        c = (a + b) / 2
        if math.isclose(f(c), 0, abs_tol=eps):
            answ.append(c)
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    # Add the found root to the list with the given precision
    answ.append((a + b) / 2)

unique_roots = remove_similar_roots(answ)
print("Equation roots: ", end="")
for root in unique_roots:
    print(root, end=" ")
```

### Advantages and Disadvantages of the Method

#### Advantages:

- <b>Guaranteed Convergence</b>: The bisection method always converges, provided the initial interval is chosen correctly (i.e., it contains a root).
- <b>Simplicity of Implementation</b>: The method is easy to program and requires minimal computation at each step.

#### Disadvantages:

- <b>Slow Convergence</b>: In the worst case, the convergence rate is linear, meaning that a large number of iterations may be required to achieve high accuracy.
- <b>Inefficiency for Multiple Roots</b>: The method may perform slowly if the equation's root is a multiple root.

### Applications
<p>&nbsp;&nbsp;&nbsp;&nbsp;The bisection method is particularly useful when a root of a function needs to be found within a specific interval and a good initial estimate is not available for other, more complex methods. It is often used as the first step in more advanced algorithms to provide a rough approximation that can then be refined by other methods.

## Newton's method

The Newton's method, also known as the method of tangents, is a numerical technique for finding the roots of nonlinear equations of the form 𝑓(𝑥) = 0. This method was proposed by Isaac Newton and is an iterative procedure that allows for finding approximate values of the roots of equations with high speed.

### The Idea Behind the Method

The method is based on using the derivative of the function 𝑓(𝑥). Suppose we have some initial approximation 𝑥0 for the root of the equation. We can improve this approximation by using a linear approximation of the function 𝑓(𝑥) at the point 𝑥0. In other words, we approximate the function with a tangent line at the point 𝑥0 and find its intersection with the x-axis.

### Newton's Method Formula

The formula for the iterative process is as follows:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/Newton.png" alt="Newton"
</p>

where:
- x<sub>𝑛</sub> is the current approximation;
- 𝑥<sub>𝑛+1</sub> is the next approximation;
- 𝑓′(𝑥<sub>𝑛) is the derivative of the function 𝑓(𝑥) at the point 𝑥<sub>𝑛</sub>.

### Steps of the Method
- <b>Choosing the initial approximation 𝑥<sub>0</sub></b>: This is the starting point from which the iteration process begins.
- <b>Calculating the new approximation 𝑥<sub>𝑛+1</sub></b>: The Newton's method formula is used.
- <b>Checking the stopping criterion</b>: If ∣ 𝑥<sub>𝑛+1 − 𝑥<sub>𝑛</sub> ∣ is sufficiently small, the iteration process stops, as the desired accuracy has been reached.

### Advantages of Newton's Method
- <b>Fast convergence</b>: Newton's method typically converges very quickly, especially if the initial guess 𝑥<sub>0</sub> is close to the root.
- <b>Wide applicability</b>: The method is suitable for solving various types of equations and systems of nonlinear equations.

### Disadvantages of Newton's Method
- <b>Dependence on the initial guess</b>: If the initial guess is poorly chosen, the method may not converge or may converge to the wrong root.
- <b>Requirement of the derivative</b>: The method requires the computation of the derivative of the function, which is not always simple or possible.
- <b>Problems with zero derivative</b>: If the derivative of the function at the point 𝑥<sub>𝑛</sub> is zero, the method cannot be applied.

### Example

Let's consider an example of finding the root of the equation 𝑓(𝑥) = $𝑥^{2}$ − 2 = 0 using Newton's method.

1. Let the initial approximation be 𝑥<sub>0</sub> = 1.
2. The function is 𝑓(𝑥) = $𝑥^{2}$ − 2, and its derivative is 𝑓′(𝑥) = 2𝑥
3. Apply Newton's method:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/Newton_ex.png" alt="Newton_ex"
</p>
and so on.

The process continues until the desired accuracy is achieved. As a result, we obtain 𝑥 ≈ 1.4142, which is a good approximation to the root $\sqrt{2}$.

Thus, Newton's method is a powerful and efficient tool for solving nonlinear equations.
