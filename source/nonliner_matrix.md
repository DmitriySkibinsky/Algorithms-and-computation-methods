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

<p>&nbsp;&nbsp;&nbsp;&nbsp;The Newton's method, also known as the method of tangents, is a numerical technique for finding the roots of nonlinear equations of the form 𝑓(𝑥) = 0. This method was proposed by Isaac Newton and is an iterative procedure that allows for finding approximate values of the roots of equations with high speed.

### The Idea Behind the Method

<p>&nbsp;&nbsp;&nbsp;&nbsp;The method is based on using the derivative of the function 𝑓(𝑥). Suppose we have some initial approximation 𝑥0 for the root of the equation. We can improve this approximation by using a linear approximation of the function 𝑓(𝑥) at the point 𝑥0. In other words, we approximate the function with a tangent line at the point 𝑥0 and find its intersection with the x-axis.

### Newton's Method Formula

<p>&nbsp;&nbsp;&nbsp;&nbsp;The formula for the iterative process is as follows:

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

### Example

<p>&nbsp;&nbsp;&nbsp;&nbsp;Let's consider an example of finding the root of the equation 𝑓(𝑥) = $𝑥^{2}$ − 2 = 0 using Newton's method.

1. Let the initial approximation be 𝑥<sub>0</sub> = 1.
2. The function is 𝑓(𝑥) = $𝑥^{2}$ − 2, and its derivative is 𝑓′(𝑥) = 2𝑥
3. Apply Newton's method:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/Newton_ex.png" alt="Newton_ex"
</p>
and so on.

The process continues until the desired accuracy is achieved. As a result, we obtain 𝑥 ≈ 1.4142, which is a good approximation to the root $\sqrt{2}$.

Thus, Newton's method is a powerful and efficient tool for solving nonlinear equations.

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
        if root > 0:
            plus_roots.append(root)
        else:
            minus_roots.append(root)

    plus_roots = plus_roots[::2]
    minus_roots = minus_roots[::2]

    # Combine the two arrays
    all_roots = minus_roots + plus_roots

    return all_roots

def f(x):
    if math.isclose(math.sin(x), 0, abs_tol=1e-9):
        return float('nan')  # Return NaN for the cases where sin(x) is close to zero
    else:
        return x - (math.cos(x) / math.sin(x))


def df(x):
    if math.isclose(math.sin(x), 0, abs_tol=1e-9):
        return float('nan')  # Return NaN for the cases where sin(x) is close to zero
    else:
        return 1 + (1 / (math.sin(x)) ** 2)


def find_roots(a, b, eps):
    roots = []
    step = 0.001  # Increased step for checking the sign of the function
    x = a

    while x < b:
        # Check if the function changes sign within the step
        if x + step <= b and f(x) * f(x + step) < 0:
            # The sign of the function changes in this interval, attempt to find a root
            x0 = x + step / 2  # Initial approximation for Newton's method
            delta = eps + 1
            while abs(delta) >= eps:
                x1 = x0 - f(x0) / df(x0)
                delta = x1 - x0
                x0 = x1
            # Check if the root is not too close to any existing root
            if not any(math.isclose(root, x1, abs_tol=eps) for root in roots):
                roots.append(x1)
        x += step
    return roots


a = float(input("Enter the coordinate A of the interval: "))
b = float(input("Enter the coordinate B of the interval: "))
eps = float(input("Enter the precision value: "))

roots = find_roots(a, b, eps)
unique_roots = remove_similar_roots(roots)
print("Found roots:", unique_roots)
```

### Advantages of Newton's Method
- <b>Fast convergence</b>: Newton's method typically converges very quickly, especially if the initial guess 𝑥<sub>0</sub> is close to the root.
- <b>Wide applicability</b>: The method is suitable for solving various types of equations and systems of nonlinear equations.

### Disadvantages of Newton's Method
- <b>Dependence on the initial guess</b>: If the initial guess is poorly chosen, the method may not converge or may converge to the wrong root.
- <b>Requirement of the derivative</b>: The method requires the computation of the derivative of the function, which is not always simple or possible.
- <b>Problems with zero derivative</b>: If the derivative of the function at the point 𝑥<sub>𝑛</sub> is zero, the method cannot be applied.

## Newton-Raphson method

The Newton-Raphson method is one of the most popular and efficient numerical methods for finding the roots of both single nonlinear equations and systems of nonlinear equations. This method is based on the idea of linear approximation of a function or a system of equations near the presumed root.

### Main Idea of the Newton-Raphson Method

The Newton-Raphson method for a single variable works as follows:

1. Start with an initial guess of the root 𝑥0.

2. Calculate the next approximation using the derivative of the function:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/Newton.png" alt="Newton"
</p>

3. Continue iterating until the function value 𝑓(𝑥) at the current approximation becomes sufficiently close to zero.

### Newton-Raphson Method for Systems of Equations

For systems of nonlinear equations, the idea is similar, but it requires dealing with multiple variables and equations. Suppose we have a system of two equations:

<p style="text-align:center;">
  f1(x,y)=0
  f2(x,y)=0
</p>

### Steps of the Method for Systems of Equations:
1. <b>Initial Guess</b>:
Start with initial guesses for the variables, for example, 𝑥0 and 𝑦0.

2. <b>Function and Jacobian Calculation</b>:
Compute the values of the system's functions at the current point, as well as the Jacobian matrix — the matrix of partial derivatives of the system's functions with respect to the variables:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/rafs1.png" alt="rafs1"
</p>

3. <b>Solving the Linear System</b>:
In each step, solve the linear system to find the increments Δ𝑥 and Δ𝑦:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/rafs2.png" alt="rafs2"
</p>
  
This is equivalent to finding the inverse of the Jacobian matrix and multiplying it by the function vector.

4. <b>Updating the Approximations</b>:
Update the variable approximations:

x<sub>n+1</sub> = x<sub>n</sub>+Δx
y<sub>n+1</sub> = y<sub>n</sub>+Δy

5. <b>Checking the Stopping Condition</b>:
Check how small the function values have become at the new points 𝑥<sub>𝑛+1</sub> and 𝑦<sub>𝑛+1</sub>. If the function value is less than the specified tolerance (e.g., 𝜖), the algorithm stops.

6. <b>Repeat Steps</b>:
If the tolerance is not met, the algorithm continues iterating.

#### For example
<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/3.%20Solution%20of%20nonlinear%20equations/img/rafs3.png" alt="rafs3"
</p>
  
```python
import math

# System of equations
def f1(x, y):
    return math.sin(y + 1) - x - 1.2

def f2(x, y):
    return 2*y + math.cos(x) - 2

# Partial derivatives of the system functions
def difx1dx(x, y):
    return -1

def dify1dy(x, y):
    return math.cos(y+1)

def difx2dx(x, y):
    return math.sin(x)*(-1)

def dify2dy(x, y):
    return 2

# Vector function F(x, y)
def Fun(x, y):
    return [f1(x, y), f2(x, y)]

# Jacobian matrix
def Jacobian(x, y):
    return [[difx1dx(x, y), dify1dy(x, y)],
            [difx2dx(x, y), dify2dy(x, y)]]

# Newton-Raphson method for the system of equations
def newtonRaphson(x0, y0, eps):
    x, y = x0, y0
    Fx = Fun(x, y)
    i = 0
    while abs(Fx[0]) > eps or abs(Fx[1]) > eps:
        J = Jacobian(x, y)
        detJ = J[0][0]*J[1][1] - J[0][1]*J[1][0]
        if abs(detJ) < eps:
            raise ValueError("The Jacobian matrix is singular, no solutions exist.")
        dx = (J[1][1]*Fx[0] - J[0][1]*Fx[1]) / detJ
        dy = (J[0][0]*Fx[1] - J[1][0]*Fx[0]) / detJ
        x -= dx
        y -= dy
        Fx = Fun(x, y)
        i += 1
    return [x, y, i]


x0 = float(input("Enter initial approximation x0: "))
y0 = float(input("Enter initial approximation y0: "))
eps = float(input("Enter accuracy eps: "))

try:
    roots = newtonRaphson(x0, y0, eps)
    print("Found roots of the system of equations: x = {}, y = {}, Number of iterations = {}".format(roots[0], roots[1], roots[2]))
except ValueError as e:
    print("Error:", e)
```

### Advantages of the Newton-Raphson Method

- <b>Fast Convergence</b>: If the initial guess is close enough to the true root, the method converges very quickly — usually with quadratic convergence.
- <b>Ease of Use</b>: The method is widely used and easy to implement for many problems.

### Disadvantages of the Method

- <b>Dependence on the Initial Guess</b>: If the initial guess is far from the true root, the method may not converge or may converge to an incorrect root.
- <b>Singularity Issues</b>: If the Jacobian matrix becomes singular (its determinant is zero), the method cannot proceed.
- <b>Requires Derivative Calculation</b>: The method requires computing and analyzing derivatives, which can be challenging for complex functions.

### Applications of the Method
The Newton-Raphson method is used in various fields, including engineering calculations, physics, optimization, and solving different nonlinear equations and systems. It is a powerful tool in numerical analysis and is often employed when a fast and efficient solution to nonlinear problems is required.
