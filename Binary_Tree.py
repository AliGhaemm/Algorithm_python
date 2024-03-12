class BinaryTree:
    class _Node:
        def __init__(self, value, left=None, right=None):
            self._value = value
            self._left = left
            self._right = right
            self._count = 1

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        if self.is_empty():
            self.root = self._Node(value)
            return
        parent = None
        pointer = self.root
        while pointer is not None:
            if value == pointer._value:
                pointer._count += 1
                return
            elif value < pointer._value:
                parent = pointer
                pointer = pointer._left
            else:
                parent = pointer
                pointer = pointer._right
        if value <= parent._value:
                parent._left = self._Node(value)
        else:
                parent._right = self._Node(value)



    def search(self, value):
        pointer = self.root
        if pointer._value == value:
            return value
        if pointer._left is not None:
            pointer._left.search(self, value)
        elif pointer._right is not  None:
            pointer._right.search(self, value)


binary_tree = BinaryTree()
binary_tree.insert(3)
binary_tree.insert(5)
binary_tree.insert(2)
binary_tree.insert(78)
binary_tree.insert(4)
binary_tree.insert(9)
binary_tree.insert(10)
binary_tree.insert(34)
binary_tree.insert(65)
binary_tree.insert(9)

