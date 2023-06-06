from itertools import combinations

def brute_force_knapsack(items, capacity):
    n = len(items)
    max_value = 0
    for r in range(n + 1):
        for subset in combinations(items, r):
            subset_weight = sum(item[0] for item in subset)
            subset_value = sum(item[1] for item in subset)
            if subset_weight <= capacity and subset_value > max_value:
                max_value = subset_value
    return max_value

items = [(2, 3), (3, 4), (4, 5), (5, 6)] 
capacity = 5
print(brute_force_knapsack(items, capacity))  

