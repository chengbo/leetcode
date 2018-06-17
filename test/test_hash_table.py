import unittest
from leetcode.hash_table.design_hash_set import MyHashSet
from leetcode.hash_table.design_hash_map import MyHashMap


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

    def test_my_hash_map(self):
        hash_map = MyHashMap()
        hash_map.put(1, 1)
        hash_map.put(2, 2)
        self.assertEqual(1, hash_map.get(1))
        self.assertEqual(-1, hash_map.get(3))
        hash_map.put(2, 1)
        self.assertEqual(1, hash_map.get(2))
        hash_map.remove(2)
        self.assertEqual(-1, hash_map.get(2))
