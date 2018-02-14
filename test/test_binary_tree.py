import unittest
from leetcode.binary_tree.tree_node import TreeNode
from leetcode.binary_tree.preorder_traversal import preorder_traversal


class TestBinaryTree(unittest.TestCase):

    def test_preorder_traversal(self):
        """
        1
         \
          2
         /
        3
        """
        node = TreeNode(1)
        node.right = TreeNode(2)
        node.right.left = TreeNode(3)

        result = preorder_traversal(node)
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
