import unittest
from leetcode.binary_tree.serialize_and_deserialize import deserialize
from leetcode.binary_search_tree.validate_binary_search_tree import is_valid_bst
from leetcode.binary_search_tree.binary_search_tree_iterator import BSTIterator


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
