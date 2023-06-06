import time
import matplotlib.pyplot as plt
import numpy as np

def measure_search_times():

    # Preparing plot variables
    sizes = range(10000, 110000, 10000)
    lin_times = []
    bin_times = []

    for size in sizes:
        arr = list(range(size))
        target = size // 2  # Middle element for best case binary search

        # Linear Search
        start = time.time()
        linear_search(arr, target)
        lin_times.append(time.time() - start)

        # Binary Search
        start = time.time()
        binary_search(arr, target)
        bin_times.append(time.time() - start)

    plt.plot(sizes, lin_times, label='Linear Search')
    plt.plot(sizes, bin_times, label='Binary Search')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

measure_search_times()
