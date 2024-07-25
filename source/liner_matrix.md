## Introduction to the Solution of Linear Equations

<p>&nbsp;&nbsp;&nbsp;&nbsp;Solving linear equations is a fundamental aspect of algebra and is pivotal in various fields such as science, engineering, economics, and computer science. Linear equations involve variables that are only to the first power, and they can represent a multitude of real-world problems, from simple budgeting calculations to complex engineering systems.

<p>&nbsp;&nbsp;&nbsp;&nbsp;A system of linear equations is a set of equations where each equation is linear. For example, a system with two variables 𝑥 and 𝑦 might look like:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/main.png" alt="main"
</p>

where 𝑎1, 𝑏1, 𝑐1, 𝑎2, 𝑏2, and 𝑐2 are constants. The goal is to find values for 𝑥 and 𝑦 that satisfy both equations simultaneously.

### Methods of Solving Linear Equations

<p>&nbsp;&nbsp;&nbsp;&nbsp;There are several methods to solve systems of linear equations:

<p>&nbsp;&nbsp;&nbsp;&nbsp;Graphical Method: Plotting each equation on a graph and finding the point(s) where they intersect.
Substitution Method: Solving one equation for one variable and substituting that expression into the other equation.
Elimination Method: Adding or subtracting equations to eliminate one variable, making it easier to solve for the remaining variable.
Matrix Methods: Using matrices and operations such as Gaussian elimination to systematically solve the system.

### Importance and Applications

<p>&nbsp;&nbsp;&nbsp;&nbsp;The ability to solve linear equations is crucial because it allows for the modeling and solving of many real-world problems. Applications range from calculating electrical circuits and optimizing production processes to financial modeling and predicting economic outcomes.

<p>&nbsp;&nbsp;&nbsp;&nbsp;Understanding and mastering these techniques provide a powerful toolset for solving a wide array of practical and theoretical problems. As systems of linear equations become larger and more complex, computational methods and software tools like MATLAB, Python, and R become essential for efficient and accurate solutions.

## Gaussian Elimination Method

<p>&nbsp;&nbsp;&nbsp;&nbsp;Gaussian elimination is a systematic method used to solve systems of linear equations. Named after the German mathematician Carl Friedrich Gauss, this method transforms a given system into an upper triangular matrix, making it easier to solve. The process involves two main stages: forward elimination and backward substitution.

<b>Forward Elimination</b>

<p>&nbsp;&nbsp;&nbsp;&nbsp;The forward elimination stage aims to transform the original system's augmented matrix into an upper triangular form. This is achieved through a series of row operations:
- <b>Pivoting</b>: For each column, identify the row with the largest absolute value in the current column (from the current row to the bottom) and swap it with the current row. This helps to avoid numerical instability.
- <b>Normalization</b>: Divide the current row by the leading coefficient (the first non-zero number in the row) to make the leading coefficient equal to 1.
- <b>Elimination</b>: Subtract multiples of the current row from the rows below it to create zeros in the column below the leading coefficient.

<p>&nbsp;&nbsp;&nbsp;&nbsp;By the end of the forward elimination stage, the augmented matrix is transformed into an upper triangular form, where all the elements below the main diagonal are zero.

<b>Backward Substitution</b>

<p>&nbsp;&nbsp;&nbsp;&nbsp;Once the matrix is in upper triangular form, the backward substitution stage begins. This stage involves solving for the variables starting from the last row and working upwards:

- <b>Starting with the last row</b>: Solve for the variable corresponding to the last row, as it will have only one variable.
- <b>Substitution</b>: Substitute the solved variable into the above rows, effectively reducing the system's size and making it easier to solve the remaining variables.
- <b>Iterate upwards</b>: Continue this process, moving up one row at a time, solving for each variable.

### Example
Consider the following system of equations:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/1.png" alt="1"
</p>

### 1. Form the augmented matrix:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/2.png" alt="2"
</p>

### 2. Forward Elimination:

- Pivot the first column if necessary and normalize the first row.
- Eliminate the x-coefficient from the second and third rows.
- Repeat for the second column, ensuring to pivot and normalize.

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/gstep.png" alt="gstep"
</p>

### 3. Backward Substitution:

- Solve the last row for z.
- Substitute z into the second row to solve for y.
- Substitute y and z into the first row to solve for x.

### Usage Example
Suppose we have the following system of linear equations:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/3.png" alt="3"
</p>

```python
def mprint(matrix, b):
    for i in range(len(matrix)):
        print(matrix[i], b[i])

def gaussian_elimination(matrix, b):
    n = len(matrix)
    for i in range(n):
        # Find the maximum element in the column
        max_element_index = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_element_index][i]):
                max_element_index = k
        # Swap rows
        matrix[i], matrix[max_element_index] = matrix[max_element_index], matrix[i]
        b[i], b[max_element_index] = b[max_element_index], b[i]

        # Divide the first element of the row by its leading coefficient
        divisor = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= divisor
        b[i] /= divisor

        # Subtract the first row from the others
        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            matrix[j][i] -= factor * matrix[i][i]
            b[j] -= factor * b[i]

    return matrix, b

matrix = [[3, 0, -1],
          [2, -5, 1],
          [2, -2, 6]]
b = [-4, 9, 8]

matrix, b = gaussian_elimination(matrix, b)
mprint(matrix, b)
```

### Importance and Applications
Gaussian elimination is a fundamental algorithm in numerical linear algebra and is widely used due to its efficiency and simplicity. Its applications include:

- <b>Engineering</b>: Solving systems of equations in circuit analysis, structural analysis, and fluid dynamics.
- <b>Computer Science</b>: Algorithms for computer graphics and machine learning models.
- <b>Economics</b>: Solving models for economic forecasting and optimization problems.
- <b>Physics</b>: Solving differential equations and quantum mechanics problems.
Understanding Gaussian elimination provides a solid foundation for more advanced numerical methods and is essential for anyone working with systems of linear equations in various scientific and engineering disciplines.

### Advantages of Gaussian Elimination

- <b>Simplicity</b>: Gaussian elimination is straightforward to understand and implement. The method relies on basic arithmetic operations (addition, subtraction, multiplication, and division), making it accessible for teaching and learning.
- <b>Systematic Procedure</b>: The method provides a clear and systematic procedure for solving systems of linear equations, which can be easily followed step-by-step.
- <b>Generality</b>: It can be applied to any system of linear equations, whether the system is small or large, consistent or inconsistent, or has a unique or infinite number of solutions.
- <b>Algorithmic Efficiency</b>: Gaussian elimination is efficient for solving systems of equations with dense matrices and is the foundation for many advanced algorithms in numerical linear algebra.
- <b>Foundation for Other Methods</b>: It forms the basis for more complex methods such as LU decomposition, which further optimizes the process for certain types of problems.

### Downsides of Gaussian Elimination

- <b>Numerical Stability</b>: Without careful implementation, Gaussian elimination can suffer from numerical instability, especially when dealing with floating-point arithmetic. Pivoting strategies (like partial or complete pivoting) are required to mitigate this issue, which adds complexity.
- <b>Computational Cost</b>: The method has a time complexity of 𝑂(𝑛^3) for an 𝑛 × 𝑛 matrix, which can become computationally expensive for very large systems. This makes it less suitable for extremely large-scale problems compared to iterative methods.
- <b>Storage Requirements</b>: Gaussian elimination requires the storage of the entire matrix, which can be impractical for very large, sparse matrices. Specialized techniques and data structures are needed to handle such cases efficiently.
- <b>Sensitive to Ill-Conditioned Systems</b>: For systems where the matrix is ill-conditioned (where small changes in the input can lead to large changes in the output), Gaussian elimination can produce inaccurate results. This sensitivity necessitates the use of preconditioning techniques or alternative methods.
- <b>Noisy Data</b>: In practical applications where data may be noisy or imprecise, the method may amplify errors, leading to unreliable solutions. Techniques such as regularization are sometimes required to stabilize the solution.

## Gauss-Seidel method

The Gauss-Seidel method (or Seidel method) is an iterative algorithm for solving a system of linear algebraic equations (SLAE) of the form 𝐴𝑥 = 𝑏, where 𝐴 is a square matrix of coefficients, 𝑥 is the vector of unknowns, and 𝑏 is the vector of constants. This method is an improvement over the simple iteration method and is one of the methods used to solve SLAEs, alongside the Jacobi and relaxation methods.

### Key Principles of the Method

<p>&nbsp;&nbsp;&nbsp;&nbsp;1. Iterative Process: The Gauss-Seidel method is based on an iterative process where each new approximation $x^{k+1}$ is obtained based on the previous approximation $x^{k}$. In each iteration, the values of the components in vector 𝑥 are updated.

<p>&nbsp;&nbsp;&nbsp;&nbsp;2. Sequential Update: Unlike the Jacobi method, where all new values are computed simultaneously, the Gauss-Seidel method uses updated values as soon as they become available. This accelerates the convergence of the method.

<p>&nbsp;&nbsp;&nbsp;&nbsp;3. Convergence: The Gauss-Seidel method converges faster than the Jacobi method if the matrix 𝐴 is diagonally dominant or positive definite. In some cases, the method may not converge, which depends on the properties of matrix 𝐴.

### Iterative Process

The iterative formula of the Gauss-Seidel method for the 𝑖-th row is as follows:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/Zendel_main.png" alt="Zendel_main"
</p>

### Example of Application

Consider an example of solving a system of equations using the Gauss-Seidel method:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/ex1.png" alt="ex1"
</p>

1. Initial approximation: $x1^{(0)}$

2. Iterations:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/ex2.png" alt="ex2"
</p>

3. Repeat iterations until the desired accuracy is achieved.

Thus, the Gauss-Seidel method is a powerful tool for solving SLAEs, especially useful for sparse and large systems, provided the convergence criteria are met.

```python
import copy
# import numpy as np

def zero_matrix(x):
    return [0] * x


def max_value(matrix):
    k = matrix[0][0]
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > k:
                k = matrix[i][j]
    return k


def zeidel(a, b, eps=1e-9):
    m = len(b)
    x = zero_matrix(m)
    d = zero_matrix(m)
    iteration = 0
    the_end = False
    while not the_end:
        # y = np.copy(x)
        y = copy.deepcopy(x)
        for i in range(m):
            s1 = sum(A[i][j] * y[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            y[i] = (b[i] - s1 - s2) / A[i][i]
            # d[i] = np.fabs (y[i] - x[i])
            d[i] = abs(y[i] - x[i])
        p = max(d)
        iteration += 1
        x = y
        the_end = p <= eps
        if iteration == 1000: the_end = True
    return x, iteration, p


A = [[2, -1, 0], [0, 5, 2], [15, -1, 3]]
B = [3, 7, 4]

x, it, p = zeidel(A, B)

print('Итерация:', it)
print('X =', x)
print('Погрешность =', p)
```
### Application

<p>&nbsp;&nbsp;&nbsp;&nbsp;The Gauss-Seidel method is particularly advantageous for solving systems of linear equations in several scenarios. It is especially useful for large, sparse systems because it efficiently updates only non-zero elements, conserving memory and computational resources. The method converges quickly for diagonally dominant or symmetric positive definite matrices, ensuring reliable solutions. It is also preferable when direct methods are computationally expensive, making it suitable for very large systems. If an approximate solution is acceptable or if a good initial guess is close to the true solution, the Gauss-Seidel method can provide quick and efficient results. Despite being less suited for parallel processing, it remains useful when parallel computing resources are limited.
  
### Advantages of Gauss-Seidel method:

- Simple to implement.
- Effective for large and sparse systems.
- Converges faster than the Jacobi method in the case of diagonally dominant matrices.

### Disadvantages of Gauss-Seidel method:

- Convergence is not guaranteed for all matrices 𝐴.
- Preliminary checking of convergence conditions may be required.
- Not as well-suited for parallel implementation as the Jacobi method.


