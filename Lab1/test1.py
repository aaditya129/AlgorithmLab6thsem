import unittest

class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.arr, 4), 3)
        self.assertEqual(linear_search(self.arr, 10), -1)

    def test_binary_search(self):
        self.assertEqual(binary_search(self.arr, 4), 3)
        self.assertEqual(binary_search(self.arr, 10), -1)

if __name__ == '__main__':
    unittest.main()
