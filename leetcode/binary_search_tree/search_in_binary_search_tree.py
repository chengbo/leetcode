def search_bst(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    if root.val > val:
        return search_bst(root.left, val)

    return search_bst(root.right, val)
