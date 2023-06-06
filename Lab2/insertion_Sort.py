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