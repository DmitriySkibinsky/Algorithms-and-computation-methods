from scipy.optimize import linprog

"""
    x1 - quantity of product type 1
    x2 - quantity of product type 2
    x3 - quantity of product type 3

    E = 13x1 + 8x2 + 4x3 => MAX 
    Multiply elements by -1 to maximize profit
"""

objective_function = [-13, -8, -4]

A_matrix = [[2, 5, 0],
            [3, 1, 1],
            [13, 4, 4]]

B_matrix = [80, 50, 210]

"""
    Additional constraint: Quantity of products cannot be negative
"""
x1_edge = x2_edge = x3_edge = (0, None)
# Solving the matrix with the additional condition
answ = linprog(objective_function, A_ub=A_matrix, b_ub=B_matrix,
               bounds=[x1_edge, x2_edge, x3_edge], method='highs')

print("Optimal solution: ")

for i, value in enumerate(answ.x):
    print(f"x{i + 1} =", value)
# Printing the value of the objective function for the optimal plan (negative sign because we are maximizing the objective)
# The value of the objective function is the maximum profit achievable under the given constraints on resources and non-negativity of variables.
print("Value of the objective function F(X) =", (-1) * answ.fun)
