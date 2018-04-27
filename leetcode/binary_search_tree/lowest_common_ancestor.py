def lca(root, p, q):
    if root is None:
        return None

    if root.val > max(p, q):
        return lca(root.left, p, q)

    if root.val < min(p, q):
        return lca(root.right, p, q)

    return root
