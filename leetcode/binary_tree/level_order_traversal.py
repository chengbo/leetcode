def level_order_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    arr = []
    __traversal(root, arr, 0)
    return arr


def __traversal(root, arr, level):
    if root is None:
        return

    if len(arr) > level:
        arr[level].append(root.val)
    else:
        arr.append([root.val])

    __traversal(root.left, arr, level + 1)
    __traversal(root.right, arr, level + 1)
