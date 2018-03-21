def connect(root):
    if not root:
        return

    if not root.left or not root.right:
        return

    root.left.next = root.right

    if root.next:
        root.right.next = root.next.left

    connect(root.left)
    connect(root.right)
