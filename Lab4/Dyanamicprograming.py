def dynamic_programming_knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1][0] <= w:
                dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

items = [(2, 3), (3, 4), (4, 5), (5, 6)]  
capacity = 5

print(dynamic_programming_knapsack(items, capacity))  
