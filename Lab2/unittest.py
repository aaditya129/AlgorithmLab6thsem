import unittest
import insertion_Sort
import merge_Sort



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

class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        self.arr = [9, 2, 5, 1, 6, 8, 3, 4, 7]
        self.sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.arr.copy()), self.sorted_arr)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.arr.copy()), self.sorted_arr)

if __name__ == '__main__':
    unittest.main()
