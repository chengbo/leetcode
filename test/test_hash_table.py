import unittest
from leetcode.hash_table.design_hash_set import MyHashSet


class TestArray(unittest.TestCase):

    def test_my_hash_set(self):
        hash_set = MyHashSet()
        hash_set.add(1)
        hash_set.add(2)
        self.assertTrue(hash_set.contains(1))
        self.assertFalse(hash_set.contains(3))
        hash_set.add(2)
        self.assertTrue(hash_set.contains(2))
        hash_set.remove(2)
        self.assertFalse(hash_set.contains(2))
