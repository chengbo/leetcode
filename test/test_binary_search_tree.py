import unittest
from leetcode.binary_tree.serialize_and_deserialize import deserialize
from leetcode.binary_search_tree.validate_binary_search_tree import is_valid_bst
from leetcode.binary_search_tree.binary_search_tree_iterator import BSTIterator
from leetcode.binary_search_tree.search_in_binary_search_tree import search_bst


class TestBinaryTree(unittest.TestCase):

    def test_is_valid_bst(self):
        """
          5
         / \
        1   4
           / \
          3   6
        """
        node1 = deserialize('5,1,#,#,4,3,#,#,6,#,#')
        self.assertFalse(is_valid_bst(node1))
        """
            8
           /  \
          3    10
         / \      \
        1   6      14
           / \    /
          4   7  13
        """
        node2 = deserialize('8,3,1,#,#,6,4,#,#,7,#,#,10,#,14,13,#,#,#')
        self.assertTrue(is_valid_bst(node2))

    def test_iterator(self):
        """
            8
           /  \
          3    10
         / \      \
        1   6      14
           / \    /
          4   7  13
        """
        node = deserialize('8,3,1,#,#,6,4,#,#,7,#,#,10,#,14,13,#,#,#')
        i, v = BSTIterator(node), []
        while i.has_next():
            v.append(i.next())
        self.assertEqual(v, [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_search_bst(self):
        """
            8
           /  \
          3    10
         / \      \
        1   6      14
           / \    /
          4   7  13
        """
        node = deserialize('8,3,1,#,#,6,4,#,#,7,#,#,10,#,14,13,#,#,#')
        node1 = search_bst(node, 3)
        self.assertEqual(node1.val, 3)
        self.assertEqual(node1.left.val, 1)
        self.assertEqual(node1.right.val, 6)
        node2 = search_bst(node, 14)
        self.assertEqual(node2.val, 14)
        self.assertEqual(node2.left.val, 13)
        self.assertIsNone(node2.right)
        node3 = search_bst(node, 9999)
        self.assertIsNone(node3)
