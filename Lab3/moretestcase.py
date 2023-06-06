import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.add(10, 'A')
        self.bst.add(20, 'B')
        self.bst.add(5, 'C')
        self.bst.add(8, 'D')
        self.bst.add(30, 'E')
        self.bst.add(15, 'F')

    def test_add(self):
        self.assertEqual(self.bst.size(), 6)
        self.assertEqual(self.bst.search(10), 'A')
        self.bst.add(6,'G')
        self.assertEqual(self.bst.search(6), 'G')
        #searching the node in the tree without adding it
        self.assertFalse(self.bst.search(100))

    def test_remove(self):
        self.assertTrue(self.bst.remove(20))
        self.assertEqual(self.bst.size(), 5)
        self.assertFalse(self.bst.search(20))
        self.assertTrue(self.bst.size(),4)
        
    def test_walk(self):
        #adding,removing nodes and checking different tree traversal
        self.bst.add(6,'H')
        self.assertEqual(self.bst.inorder_walk(), [5, 6, 8, 10, 15, 20, 30])
        self.bst.remove(5)
        self.assertEqual(self.bst.postorder_walk(), [8,15,30,20,10])
        self.bst.remove(20)
        self.assertEqual(self.bst.preorder_walk(), [10,8,15,30])

    def test_size(self):
        self.assertEqual(self.bst.size(), 6)
        self.bst.remove(20)
        self.assertEqual(self.bst.size(), 5)
        self.bst.add(40, 'G')
        self.assertEqual(self.bst.size(), 6)

if __name__ == "__main__":
    unittest.main()