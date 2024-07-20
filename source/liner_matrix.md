## Introduction to the Solution of Linear Equations

<p>&nbsp;&nbsp;&nbsp;&nbsp;Solving linear equations is a fundamental aspect of algebra and is pivotal in various fields such as science, engineering, economics, and computer science. Linear equations involve variables that are only to the first power, and they can represent a multitude of real-world problems, from simple budgeting calculations to complex engineering systems.

<p>&nbsp;&nbsp;&nbsp;&nbsp;A system of linear equations is a set of equations where each equation is linear. For example, a system with two variables 𝑥 and 𝑦 might look like:

<p align="center">
  <img src="https://github.com/DmitriySkibinsky/Algorithms-and-computation-methods/blob/main/source/2.%20Solution%20of%20linear%20equations/img/main.png" alt="main"
</p>

where 𝑎1, 𝑏1, 𝑐1, 𝑎2, 𝑏2, and 𝑐2 are constants. The goal is to find values for 𝑥 and 𝑦 that satisfy both equations simultaneously.

### Methods of Solving Linear Equations

There are several methods to solve systems of linear equations:

Graphical Method: Plotting each equation on a graph and finding the point(s) where they intersect.
Substitution Method: Solving one equation for one variable and substituting that expression into the other equation.
Elimination Method: Adding or subtracting equations to eliminate one variable, making it easier to solve for the remaining variable.
Matrix Methods: Using matrices and operations such as Gaussian elimination to systematically solve the system.

### Importance and Applications

The ability to solve linear equations is crucial because it allows for the modeling and solving of many real-world problems. Applications range from calculating electrical circuits and optimizing production processes to financial modeling and predicting economic outcomes.

Understanding and mastering these techniques provide a powerful toolset for solving a wide array of practical and theoretical problems. As systems of linear equations become larger and more complex, computational methods and software tools like MATLAB, Python, and R become essential for efficient and accurate solutions.

## Gaussian Elimination Method

<p>&nbsp;&nbsp;&nbsp;&nbsp;Gaussian elimination is a systematic method used to solve systems of linear equations. Named after the German mathematician Carl Friedrich Gauss, this method transforms a given system into an upper triangular matrix, making it easier to solve. The process involves two main stages: forward elimination and backward substitution.

<b>Forward Elimination</b>

The forward elimination stage aims to transform the original system's augmented matrix into an upper triangular form. This is achieved through a series of row operations:
- <b>Pivoting</b>: For each column, identify the row with the largest absolute value in the current column (from the current row to the bottom) and swap it with the current row. This helps to avoid numerical instability.
- <b>Normalization</b>: Divide the current row by the leading coefficient (the first non-zero number in the row) to make the leading coefficient equal to 1.
- <b>Elimination</b>: Subtract multiples of the current row from the rows below it to create zeros in the column below the leading coefficient.

By the end of the forward elimination stage, the augmented matrix is transformed into an upper triangular form, where all the elements below the main diagonal are zero.

<b>Backward Substitution</b>

Once the matrix is in upper triangular form, the backward substitution stage begins. This stage involves solving for the variables starting from the last row and working upwards:

- <b>Starting with the last row</b>: Solve for the variable corresponding to the last row, as it will have only one variable.
- <b>Substitution</b>: Substitute the solved variable into the above rows, effectively reducing the system's size and making it easier to solve the remaining variables.
- <b>Iterate upwards</b>: Continue this process, moving up one row at a time, solving for each variable.
