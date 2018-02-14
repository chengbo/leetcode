def inorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    result = inorder_traversal(root.left)
    result += [root.val]
    result += inorder_traversal(root.right)

    return result
