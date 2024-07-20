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
