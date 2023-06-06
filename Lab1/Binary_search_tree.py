# Node class
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Function to insert nodes in the BST
def insert(node, data):

    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node
# Function to perform binary search on the BST
def binary_search_tree(node, target):
    if node is None or node.data == target:
        return node

    if node.data < target:
        return binary_search_tree(node.right, target)

    return binary_search_tree(node.left, target)

# Function to perform Linear search 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Driver program to test the above functions
root = None
keys = [8, 3, 1, 6, 7, 10, 14, 4]

for key in keys:
    root = insert(root, key)

result = binary_search_tree(root, 100)

if result:
    print("Found")
else:
    print("Not found")
