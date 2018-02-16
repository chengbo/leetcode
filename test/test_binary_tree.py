import unittest
from leetcode.binary_tree.tree_node import TreeNode
from leetcode.binary_tree.preorder_traversal import preorder_traversal
from leetcode.binary_tree.inorder_traversal import inorder_traversal
from leetcode.binary_tree.postorder_traversal import postorder_traversal


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

    def test_inorder_traversal(self):
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

        result = inorder_traversal(node)
        self.assertEqual(result, [1, 3, 2])

    def test_postorder_traversal(self):
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

        result = postorder_traversal(node)
        self.assertEqual(result, [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
