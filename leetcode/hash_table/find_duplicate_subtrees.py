import collections


def find_duplicate_subtrees(root):

    nodes = collections.defaultdict(list)

    def traversal(node):
        if node is None:
            return '#'
        s = f'{node.val},{traversal(node.left)},{traversal(node.right)}'
        nodes[s].append(node)
        return s

    traversal(root)
    return [nodes[s][0] for s in nodes.keys() if len(nodes[s]) > 1]
