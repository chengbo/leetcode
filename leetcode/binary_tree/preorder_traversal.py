def preorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    result = [root.val]

    result += preorder_traversal(root.left)
    result += preorder_traversal(root.right)

    return result
