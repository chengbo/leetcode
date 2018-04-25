def delete_node(root, key):
    if root is None:
        return None

    if root.val > key:
        root.left = delete_node(root.left, key)
        return root

    if root.val < key:
        root.right = delete_node(root.right, key)
        return root

    if root.left is None:
        return root.right

    if root.right is None:
        return root.left

    max_node = root.left
    while root.right is not None:
        root = root.right

    root.val = max_node.val
    root.left = delete_node(root.left, max_node.val)
    return root
