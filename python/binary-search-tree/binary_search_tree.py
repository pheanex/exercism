class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        node = self.root
        while node:
            if node.value < value:
                if not node.right:
                    node.right = TreeNode(value)
                    return
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(value)
                    return
                node = node.left

    def search(self, value):
        node = self.root
        while node:
            if node.value == value:
                return node
            if node.value < value:
                node = node.right
            else:
                node = node.left
        return None

    def traverse(self, node):
        if not node:
            return
        yield from self.traverse(node.left)
        yield node
        yield from self.traverse(node.right)

    def list(self):
        return [node.value for node in self.traverse(self.root)]
