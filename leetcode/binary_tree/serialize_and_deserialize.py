from leetcode.binary_tree.tree_node import TreeNode


def serialize(root):
    result = []
    def write(root):
        if not root:
            result.append('#')
            return
        result.append(str(root.val))
        write(root.left)
        write(root.right)

    write(root)
    return ','.join(result)


def deserialize(data):
    def read(array):
        c = next(array)
        if c == '#':
            return None
        node = TreeNode(int(c))
        node.left = read(array)
        node.right = read(array)
        return node

    array = iter(data.split(','))
    return read(array)
