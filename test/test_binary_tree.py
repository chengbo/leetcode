import unittest
from leetcode.binary_tree.tree_node import TreeNode
from leetcode.binary_tree.preorder_traversal import preorder_traversal
from leetcode.binary_tree.inorder_traversal import inorder_traversal
from leetcode.binary_tree.postorder_traversal import postorder_traversal
from leetcode.binary_tree.level_order_traversal import level_order_traversal
from leetcode.binary_tree.maximum_depth import maximum_depth, maximum_depth2
from leetcode.binary_tree.symmetric_tree import is_symmetric_tree
from leetcode.binary_tree.path_sum import has_path_sum
from leetcode.binary_tree.construct_binary_tree import build_tree_from_i_and_p


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

    def test_level_order_traversal(self):
        """
          3
         / \
        9  20
          /  \
         15   7
        """
        node = TreeNode(3)
        node.left = TreeNode(9)
        node.right = TreeNode(20)
        node.right.left = TreeNode(15)
        node.right.right = TreeNode(7)

        result = level_order_traversal(node)
        self.assertEqual(result, [[3], [9, 20], [15, 7]])

    def test_maximum_depth(self):
        """
          3
         / \
        9  20
          /  \
         15   7
        """
        node = TreeNode(3)
        node.left = TreeNode(9)
        node.right = TreeNode(20)
        node.right.left = TreeNode(15)
        node.right.right = TreeNode(7)

        result = maximum_depth(node)
        self.assertEqual(result, 3)

        result = maximum_depth2(node, 0)
        self.assertEqual(result, 3)

    def test_symmetric_tree(self):
        """
            1
           / \
          2   2
         / \ / \
        3  4 4  3
        """
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.left.left = TreeNode(3)
        node.left.right = TreeNode(4)
        node.right = TreeNode(2)
        node.right.left = TreeNode(4)
        node.right.right = TreeNode(3)

        result = is_symmetric_tree(node)
        self.assertTrue(result)

        """
          1
         / \
        2   2
         \   \
         3    3
        """
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.left.right = TreeNode(3)
        node.right = TreeNode(2)
        node.right.right = TreeNode(3)

        result = is_symmetric_tree(node)
        self.assertFalse(result)

    def test_has_path_sum(self):
        """
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        """
        node = TreeNode(5)
        node.left = TreeNode(4)
        node.left.left = TreeNode(11)
        node.left.left.left = TreeNode(7)
        node.left.left.right = TreeNode(2)
        node.right = TreeNode(8)
        node.right.left = TreeNode(13)
        node.right.right = TreeNode(4)
        node.right.right.right = TreeNode(1)

        result = has_path_sum(node, 22)
        self.assertTrue(result)

    def test_build_tree_from_i_and_p(self):
        """
          3
         / \
        9  20
          /  \
         15   7
        """
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]

        node = build_tree_from_i_and_p(inorder, postorder)
        self.assertEqual(node.val, 3)
        self.assertTrue(node.left.val, 9)
        self.assertTrue(node.right.val, 20)
        self.assertTrue(node.right.left.val, 15)
        self.assertTrue(node.right.right.val, 7)


if __name__ == '__main__':
    unittest.main()
