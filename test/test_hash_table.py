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
from leetcode.hash_table.contains_duplicate_ii import contains_nearby_duplicate
from leetcode.hash_table.group_anagrams import group_anagrams
from leetcode.hash_table.valid_sudoku import is_valid_sudoku
from leetcode.hash_table.find_duplicate_subtrees import find_duplicate_subtrees
from leetcode.binary_tree.serialize_and_deserialize import deserialize


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
        list2 = [
            "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
            "Shogun"
        ]
        self.assertEqual(["Shogun"], find_restaurant(list1, list2))

        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["KFC", "Shogun", "Burger King"]
        self.assertEqual(["Shogun"], find_restaurant(list1, list2))

        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Tapioca Express", "Shogun", "Burger King"]
        self.assertEqual(["Tapioca Express", "Shogun"],
                         find_restaurant(list1, list2))

    def test_first_uniq_char(self):
        self.assertEqual(0, first_uniq_char('leetcode'))
        self.assertEqual(2, first_uniq_char('loveleetcode'))

    def test_intersect(self):
        self.assertEqual([2, 2], intersect([1, 2, 2, 1], [2, 2]))
        self.assertEqual([1], intersect([1], [1, 1]))
        self.assertEqual([1], intersect([1, 2], [1, 1]))

    def test_contains_nearby_duplicate(self):
        self.assertTrue(contains_nearby_duplicate([1, 2, 3, 1], 3))
        self.assertTrue(contains_nearby_duplicate([1, 0, 1, 1], 1))
        self.assertFalse(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

    def test_group_anagrams(self):
        strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        expected = [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        result = group_anagrams(strs)
        for i in range(len(expected)):
            self.assertEqual(sorted(result[i]), sorted(expected[i]))

    def test_is_valid_sudoku(self):
        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]  # yapf: disable
        self.assertTrue(is_valid_sudoku(board))
        board = [
            ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]  # yapf: diable
        self.assertFalse(is_valid_sudoku(board))

        board = [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."]
        ]  # yapf: diable
        self.assertFalse(is_valid_sudoku(board))

    def test_find_duplicate_subtrees(self):
        """
            1
           / \
          2   3
         /   / \
        4   2   4
           /
          4
        """
        root = deserialize('1,2,4,#,#,#,3,2,4,#,#,#,4,#,#')
        result = find_duplicate_subtrees(root)
        self.assertEqual(4, result[0].val)
        self.assertEqual(2, result[1].val)
