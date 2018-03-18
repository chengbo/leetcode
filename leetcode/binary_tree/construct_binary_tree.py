from leetcode.binary_tree.tree_node import TreeNode


def build_tree_from_i_and_p(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder[-1]
    node = TreeNode(root_val)
    i = inorder.index(root_val)
    node.left = build_tree_from_i_and_p(inorder[:i], postorder[:i])
    node.right = build_tree_from_i_and_p(inorder[i + 1:], postorder[i:-1])
    return node


def build_tree_from_p_and_i(preorder, inorder):
    if not inorder:
        return None

    root_val = preorder.pop(0)
    node = TreeNode(root_val)
    i = inorder.index(root_val)
    node.left = build_tree_from_p_and_i(preorder, inorder[:i])
    node.right = build_tree_from_p_and_i(preorder, inorder[i + 1:])
    return node
