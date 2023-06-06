import time
import matplotlib.pyplot as plt
import numpy as np
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


keys = [8, 3, 1, 6, 7, 10, 14, 4]

result = insertion_sort(keys)

print(result)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged



result2 = merge_sort(keys)
print(result2)

def measure_sort_times():

    sizes = range(1000, 10000, 1000)
    ins_times = []
    merge_times = []

    for size in sizes:
        arr = random.sample(range(1, size + 1), size)

        start = time.time()
        insertion_sort(arr.copy())
        ins_times.append(time.time() - start)

        start = time.time()
        merge_sort(arr.copy())
        merge_times.append(time.time() - start)

    plt.plot(sizes, ins_times, label='Insertion Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

measure_sort_times()
