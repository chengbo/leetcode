from leetcode.binary_tree.tree_node import TreeNode


def insert_into_bst(root, val):
    if root is None:
        return None

    if root.val == val:
        raise Exception('invalid val')

    if root.val > val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insert_into_bst(root.left, val)
    else:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            insert_into_bst(root.right, val)

    return root
