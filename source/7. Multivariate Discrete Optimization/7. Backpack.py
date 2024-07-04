def knapsack(capacity, weights, values, n):
    # Create a 2D array to store the results of subproblems
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the weight of the i-th item is more than the current capacity j,
            # then we cannot include this item in the knapsack
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            # Otherwise, we can choose whether to include the i-th item in the knapsack or not
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    # Retrieve the list of values and indices of selected items
    selected_values = []
    selected_items = []
    weight_remaining = capacity
    for i in range(n, 0, -1):
        if dp[i][weight_remaining] != dp[i - 1][weight_remaining]:
            selected_values.append(values[i - 1])
            selected_items.append(i)  # Add the item number
            weight_remaining -= weights[i - 1]

    # Return the maximum value, list of values of selected items, list of indices of selected items, and remaining capacity
    return dp[n][capacity], selected_values, selected_items, weight_remaining

# Example usage
capacity = 15
weights = [6, 4, 3, 2, 5]
values = [5, 3, 1, 3, 6]
n = len(weights)
max_value, selected_values, selected_items, weight_remaining = knapsack(capacity, weights, values, n)

print(f"Maximum value that can be placed in the knapsack: {max_value}")
print("Values of selected items:", selected_values)
print("Indices of selected items:", selected_items)
print(f"Remaining capacity of the knapsack: {weight_remaining}")
