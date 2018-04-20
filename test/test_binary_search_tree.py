import unittest
from leetcode.binary_tree.serialize_and_deserialize import deserialize
from leetcode.binary_search_tree.validate_binary_search_tree import is_valid_bst


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
