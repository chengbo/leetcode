def is_balanced(root):
    if root is None:
        return True

    l_height = height(root.left)
    r_height = height(root.right)
    return abs(l_height - r_height) <= 1 and is_balanced(root.left) and \
        is_balanced(root.right)


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1
