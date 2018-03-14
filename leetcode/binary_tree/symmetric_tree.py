def is_symmetric_tree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True

    return mirror_equals(root.left, root.right)


def mirror_equals(l_node, r_node):
    if not l_node or not r_node:
        return not l_node and not r_node

    return l_node.val == r_node.val and \
        mirror_equals(l_node.left, r_node.right) and \
        mirror_equals(l_node.right, r_node.left)
