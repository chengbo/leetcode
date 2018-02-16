def postorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    result = postorder_traversal(root.left)
    result += postorder_traversal(root.right)

    result += [root.val]
    return result
