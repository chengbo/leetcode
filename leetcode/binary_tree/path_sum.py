def has_path_sum(root, sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == sum

    return has_path_sum(root.left, sum - root.val) or \
        has_path_sum(root.right, sum - root.val)
