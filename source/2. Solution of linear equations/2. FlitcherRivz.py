import numpy as np

def fletcher_reeves_method(A, B):
    # Initial approximation X0
    X = np.zeros(len(B))

    # Compute the gradient at X0
    gradient = np.dot(A, X) - B

    # Initial value for the descent direction D
    D = -gradient

    # Iteration counter
    iteration = 0
    max_iterations = 100

    # Solution precision
    epsilon = 0.00001

    # While the gradient norm is greater than epsilon and the maximum number of iterations is not reached
    while np.dot(gradient, gradient) > epsilon and iteration < max_iterations:
        # Compute the function value at the current iteration
        f = np.dot(gradient, gradient)

        # Compute the value of alpha for the current iteration
        alpha = f / np.dot(np.dot(A, D), D)

        # Update the value of X
        X = X - alpha * D

        # Update the value of the gradient
        new_gradient = np.dot(A, X) - B

        # Compute the value of beta for the current iteration
        beta = np.dot(new_gradient, new_gradient) / np.dot(gradient, gradient)

        # Update the value of the descent direction
        D = -new_gradient + beta * D

        # Update the value of the gradient
        gradient = new_gradient

        iteration += 1

    return X

# Example usage
A = np.array([[4, 1], [1, 3]])
B = np.array([1, 2])
solution = fletcher_reeves_method(A, B)
print("Solution:", solution)