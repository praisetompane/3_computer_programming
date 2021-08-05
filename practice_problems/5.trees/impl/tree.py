class BinaryTreeNode:
    data = None
    left = None
    right = None

    def __init__(self, root, left, right):
        self.data = root
        self.left = left
        self.right = right

    #left, parent, right
    def in_order_print(self):
        if(self.left is not None):
            print(self.left.data)
        print(self.data)
        if(self.right is not None):
            print(self.right.data)

    #parent, left, right
    def pre_order_print(self):
        print(self.data)
        if(self.left is not None):
            print(self.left.data)
        if(self.right is not None):
            print(self.right.data)

    #left, right, parent
    def post_order_print(self):
        if(self.left is not None):
            print(self.left.data)
        if(self.right is not None):
            print(self.right.data)
        print(self.data)


class BinaryTree:
    root = None

    def __init__(self, root):
        n = BinaryTreeNode(root, None, None)
        self.root = n

    def _in_order_traversal(self, node, process):
        if(node is not None):
            self._in_order_traversal(node.left, process)
            process(node.data)
            self._in_order_traversal(node.right, process)

    def in_order_print(self):
        self._in_order_traversal(self.root, print)

    def _pre_order_traversal(self, node, process):
        if(node is not None):
            process(node.data)
            self._pre_order_traversal(node.left, process)
            self._pre_order_traversal(node.right, process)

    def pre_order_print(self):
        self._pre_order_traversal(self.root, print)

    def _post_order_traversal(self, node, process):
        if(node is not None):
            self._post_order_traversal(node.left, process)
            self._post_order_traversal(node.right, process)
            process(node.data)

    def post_order_print(self):
        self._post_order_traversal(self.root, print)


if __name__ == '__main__':
    tree = BinaryTree(3)

    tree.in_order_print()
