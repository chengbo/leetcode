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


def connect_ii(root):
    if not root:
        return

    parent = root
    prev = None
    head = None

    while parent:
        if parent.left:
            if head:
                prev.next = parent.left
            else:
                head = parent.left
            prev = parent.left

        if parent.right:
            if head:
                prev.next = parent.right
            else:
                head = parent.right
            prev = parent.right

        parent = parent.next

        if not parent:
            parent = head
            prev = None
            head = None
