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


def morris_inorder_traversal(root):
    current = root
    result = []

    while current is not None:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and \
                    predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result
