def greedy_fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item[0]:
            total_value += item[1]
            capacity -= item[0]
        else:
            fraction = capacity / item[0]
            total_value += item[1] * fraction
            break
    return total_value


items = [(2, 3), (3, 4), (4, 5), (5, 6)]  
capacity = 5

print(greedy_fractional_knapsack(items, capacity)) 

