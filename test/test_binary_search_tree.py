import unittest
from leetcode.binary_tree.preorder_traversal import preorder_traversal
from leetcode.binary_tree.serialize_and_deserialize import deserialize
from leetcode.binary_search_tree.validate_binary_search_tree import is_valid_bst
from leetcode.binary_search_tree.binary_search_tree_iterator import BSTIterator
from leetcode.binary_search_tree.search_in_binary_search_tree import search_bst
from leetcode.binary_search_tree.insert_into_a_binary_search_tree import (
    insert_into_bst)
from leetcode.binary_search_tree.delete_node_in_a_bst import delete_node
from leetcode.binary_search_tree.lowest_common_ancestor import lca
from leetcode.binary_search_tree.balanced import is_balanced


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

    def test_insert_into_bst(self):
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
        node1 = insert_into_bst(node, 2)
        node2 = insert_into_bst(node, 15)
        self.assertTrue(is_valid_bst(node1))
        self.assertTrue(is_valid_bst(node2))
        self.assertEqual(node1.left.left.right.val, 2)
        self.assertEqual(node2.right.right.right.val, 15)

    def test_delete_node(self):
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
        node1 = delete_node(node, 1)
        self.assertEqual(preorder_traversal(node1), [
                         8, 3, 6, 4, 7, 10, 14, 13])
        node = deserialize('8,3,1,#,#,6,4,#,#,7,#,#,10,#,14,13,#,#,#')
        node2 = delete_node(node, 10)
        self.assertEqual(preorder_traversal(node2), [
                         8, 3, 1, 6, 4, 7, 14, 13])
        node = deserialize('8,3,1,#,#,6,4,#,#,7,#,#,10,#,14,13,#,#,#')
        node3 = delete_node(node, 14)
        self.assertEqual(preorder_traversal(node3), [
                         8, 3, 1, 6, 4, 7, 10, 13])

    def test_lca(self):
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
        self.assertEqual(lca(node, 1, 14).val, 8)
        self.assertEqual(lca(node, 1, 7).val, 3)
        self.assertEqual(lca(node, 13, 10).val, 10)

    def test_is_balanced(self):
        """
           3
          / \
         9  20
           /  \
          15   7
        """
        node = deserialize('3,9,#,#,20,15,#,#,7,#,#')
        self.assertTrue(is_balanced(node))
        """
               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        """
        node = deserialize('1,2,3,4,#,#,4,#,#,3,#,#,2,#,#')
        self.assertFalse(is_balanced(node))
