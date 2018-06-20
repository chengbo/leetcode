import unittest
from leetcode.hash_table.design_hash_set import MyHashSet
from leetcode.hash_table.design_hash_map import MyHashMap
from leetcode.hash_table.contains_duplicate import contains_duplicate
from leetcode.hash_table.single_number import single_number
from leetcode.hash_table.intersection_of_two_arrays import intersection
from leetcode.hash_table.happy_number import is_happy
from leetcode.hash_table.two_sum import two_sum
from leetcode.hash_table.isomorphic_strings import is_isomorphic
from leetcode.hash_table.minimum_index_sum_of_two_lists import find_restaurant
from leetcode.hash_table.first_unique_character_in_a_string import first_uniq_char
from leetcode.hash_table.intersection_of_two_arrays_ii import intersect


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

    def test_contains_duplicate(self):
        self.assertFalse(contains_duplicate(None))
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))
        self.assertTrue(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_single_number(self):
        self.assertEqual(1, single_number([2, 2, 1]))
        self.assertEqual(4, single_number([4, 1, 2, 1, 2]))

    def test_intersection(self):
        self.assertEqual([2], intersection([1, 2, 2, 1], [2, 2]))

    def test_is_happy(self):
        self.assertTrue(is_happy(19))
        self.assertTrue(is_happy(7))
        self.assertFalse(is_happy(2))

    def test_two_sum(self):
        self.assertEqual([0, 1], two_sum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], two_sum([2, 7, 11, 15], 18))
        self.assertEqual([1, 2], two_sum([3, 2, 4], 6))
        self.assertEqual([0, 1], two_sum([3, 3], 6))

    def test_is_isomorphic(self):
        self.assertTrue(is_isomorphic('egg', 'add'))
        self.assertFalse(is_isomorphic('foo', 'bar'))
        self.assertTrue(is_isomorphic('paper', 'title'))
        self.assertFalse(is_isomorphic('ab', 'aa'))

    def test_find_restaurant(self):
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        self.assertEqual(["Shogun"], find_restaurant(list1, list2))

        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["KFC", "Shogun", "Burger King"]
        self.assertEqual(["Shogun"], find_restaurant(list1, list2))

        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Tapioca Express", "Shogun", "Burger King"]
        self.assertEqual(["Tapioca Express", "Shogun"], find_restaurant(list1, list2))

    def test_first_uniq_char(self):
        self.assertEqual(0, first_uniq_char('leetcode'))
        self.assertEqual(2, first_uniq_char('loveleetcode'))

    def test_intersect(self):
        self.assertEqual([2, 2], intersect([1, 2, 2, 1], [2, 2]))
        self.assertEqual([1], intersect([1], [1, 1]))
        self.assertEqual([1], intersect([1, 2], [1, 1]))
