class BSTIterator:
    def __init__(self, root):
        self.current = root
        self.stack = []

    def has_next(self):
        return self.current or len(self.stack) > 0

    def next(self):
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        node = self.stack.pop()
        self.current = node.right
        return node.val
