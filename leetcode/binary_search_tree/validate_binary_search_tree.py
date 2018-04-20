def is_valid_bst(root):
    current = root
    prev = None

    while current is not None:
        if current.left is None:
            if prev is not None and prev.val >= current.val:
                return False
            prev = current
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                if prev is not None and prev.val >= current.val:
                    return False
                prev = current
                predecessor.right = None
                current = current.right

    return True
