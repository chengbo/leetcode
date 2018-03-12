def maximum_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0

    left_result = maximum_depth(root.left)
    right_result = maximum_depth(root.right)

    return max(left_result, right_result) + 1


def maximum_depth2(root, depth):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return depth

    left_result = maximum_depth2(root.left, depth + 1)
    right_result = maximum_depth2(root.right, depth + 1)

    return max(left_result, right_result)
