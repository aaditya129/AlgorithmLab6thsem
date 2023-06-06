class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def add(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self._add(key, value, self.root)
        self.num_nodes += 1

    def _add(self, key, value, node):
        if key < node.key:
            if node.left is not None:
                self._add(key, value, node.left)
            else:
                node.left = Node(key, value)
        else:
            if node.right is not None:
                self._add(key, value, node.right)
            else:
                node.right = Node(key, value)

    def search(self, key):
        if self.root is not None:
            result = self._search(key, self.root)
            if result:
                return result.value
            else:
                return False
        else:
            return False

    def _search(self, key, node):
        if key == node.key:
            return node
        elif (key < node.key and node.left is not None):
            return self._search(key, node.left)
        elif (key > node.key and node.right is not None):
            return self._search(key, node.right)

    def remove(self, key):
        self.root, deleted = self._remove(self.root, key)
        if deleted:
            self.num_nodes -= 1
        return deleted

    def _remove(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._remove(node.left, key)
        elif key > node.key:
            node.right, deleted = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            min_right = self._min_value_node(node.right)
            node.key, node.value = min_right.key, min_right.value
            node.right, _ = self._remove(node.right, min_right.key)
            return node, True

        return node, deleted

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_walk(self):
        return self._inorder_walk(self.root, [])

    def _inorder_walk(self, node, arr):
        if node is not None:
            self._inorder_walk(node.left, arr)
            arr.append(node.key)
            self._inorder_walk(node.right, arr)
        return arr

    def preorder_walk(self):
        return self._preorder_walk(self.root, [])

    def _preorder_walk(self, node, arr):
        if node is not None:
            arr.append(node.key)
            self._preorder_walk(node.left, arr)
            self._preorder_walk(node.right, arr)
        return arr

    def postorder_walk(self):
        return self._postorder_walk(self.root, [])

    def _postorder_walk(self, node, arr):
        if node is not None:
            self._postorder_walk(node.left, arr)
            self._postorder_walk(node.right, arr)
            arr.append(node.key)
        return arr


