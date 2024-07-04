import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def vstack_algorithm(arrays):
    # Step 1: Initialize an empty list to store the stacked arrays
    stacked_arrays = []

    # Step 2: Iterate over each array in the sequence
    for arr in arrays:
        # Step 3: Check if the array is one-dimensional
        if isinstance(arr[0], (int, float)):
            # Step 4: Convert it to a two-dimensional array with one row
            stacked_arrays.append([arr])
        elif isinstance(arr[0], list) and isinstance(arr[0][0], (int, float)):
            # Step 5: Add the converted array to the list of stacked arrays
            stacked_arrays.append(arr)
        else:
            # If it is not a one-dimensional or two-dimensional array, raise an error
            raise ValueError("All arrays must be one-dimensional or two-dimensional")

    # Step 6: Combine the stacked arrays vertically to form the final stacked array
    return [row for sublist in stacked_arrays for row in sublist]

def Tikhonov_reg(A, b, alpha):
    # Function takes matrix A, vector b, and parameter alpha
    # Determine the size of matrix A
    m, n = len(A), len(A[0])
    # Define the regularized matrix A
    A_tikh = vstack_algorithm(A + [[alpha if i == j else 0 for j in range(n)] for i in range(n)])
    # Define the regularized vector b
    b_tikh = vstack_algorithm(b + [[0] for _ in range(n)])
    # Find the solution of the system of equations using the least squares method
    x_tikh = np.linalg.lstsq(A_tikh, b_tikh, rcond=None)[0]
    # Return the regularized matrices A and b
    return A_tikh, b_tikh, x_tikh

# Function to visualize the solution
def visualize_solution(A, b, x_tikh, alpha):
    # Determine the size of matrix A
    m, n = len(A), len(A[0])

    # Visualize the regularized matrix A
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.matshow(A_tikh, cmap='viridis')
    ax.set_title(f'Regularized matrix A (alpha = {alpha})')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Rows')
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(m))
    plt.colorbar(ax.matshow(A_tikh, cmap='viridis'), ax=ax)
    plt.show()

    # Visualize the regularized vector b
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(np.arange(len(b_tikh)), [row[0] for row in b_tikh])
    ax.set_title(f'Regularized vector b (alpha = {alpha})')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.show()

    # Visualize the solution
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_tikh, 'o-')
    ax.set_title(f'Solution of the system with Tikhonov regularization (alpha = {alpha})')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.show()

# Example usage
A = [[2, -1,  50], [80, 5, 2], [100, -1, 3]]
b = [[3], [7], [4]]
alpha = 0.1
A_tikh, b_tikh, x_tikh = Tikhonov_reg(A, b, alpha)

answ = []
for i in range(3):
    answ.append(x_tikh[i][0])

# visualize_solution(A, b, x_tikh, alpha)
print("Matrix roots: ", answ)
print("Regularized matrix A:")
for row in A_tikh:
    print(row)
print("Regularized vector b:")
for row in b_tikh:
    print(row)
