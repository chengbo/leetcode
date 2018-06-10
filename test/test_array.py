import unittest
from leetcode.array.find_pivot_index import find_pivot_index
from leetcode.array.largest_number_at_least_twice_of_others import dominant_index
from leetcode.array.plus_one import plus_one
from leetcode.array.diagonal_traverse import find_diagonal_order
from leetcode.array.spiral_matrix import spiral_order
from leetcode.array.pascals_triangle import generate
from leetcode.array.add_binary import add_binary
from leetcode.array.implement_strstr import str_str
from leetcode.array.longest_common_prefix import longest_common_prefix
from leetcode.array.reverse_string import reverse_string
from leetcode.array.array_partition_i import array_pair_sum
from leetcode.array.two_sum_ii import two_sum
from leetcode.array.remove_element import remove_element
from leetcode.array.max_consecutive_ones import find_max_consecutive_ones
from leetcode.array.minimum_size_subarray_sum import min_sub_array_len
from leetcode.array.rotate_array import rotate
from leetcode.array.pascals_triangle_ii import get_row


class TestArray(unittest.TestCase):

    def test_find_pivot_index(self):
        array = [1, 7, 3, 6, 5, 6]
        self.assertEqual(3, find_pivot_index(array))

        array = [1, 2, 3]
        self.assertEqual(-1, find_pivot_index(array))

    def test_dominant_index(self):
        array = [1]
        self.assertEqual(0, dominant_index(array))

        array = [3, 6, 1, 0]
        self.assertEqual(1, dominant_index(array))

        array = [1, 2, 3, 4]
        self.assertEqual(-1, dominant_index(array))

    def test_plus_one(self):
        digits = [1, 2, 3]
        self.assertEqual([1, 2, 4], plus_one(digits))

        digits = [4, 3, 2, 1]
        self.assertEqual([4, 3, 2, 2], plus_one(digits))

        digits = [9, 9, 9]
        self.assertEqual([1, 0, 0, 0], plus_one(digits))

    def test_find_diagonal_order(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual([1, 2, 4, 7, 5, 3, 6, 8, 9],
                         find_diagonal_order(matrix))

    def test_spiral_order(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], spiral_order(matrix))

        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9,
                          5, 6, 7], spiral_order(matrix))

    def test_generate_pascals_triangle(self):
        result = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(result, generate(5))

    def test_add_binary(self):
        a, b = '', '1'
        self.assertEqual('1', add_binary(a, b))

        a, b = '11', '1'
        self.assertEqual('100', add_binary(a, b))

        a, b = '1010', '1011'
        self.assertEqual('10101', add_binary(a, b))

    def test_str_str(self):
        haystack, needle = "hello", ""
        self.assertEqual(0, str_str(haystack, needle))

        haystack, needle = "hello", "ll"
        self.assertEqual(2, str_str(haystack, needle))

        haystack, needle = "aaaaa", "bba"
        self.assertEqual(-1, str_str(haystack, needle))

        haystack, needle = "hello", "oa"
        self.assertEqual(-1, str_str(haystack, needle))

        haystack, needle = "aaa", "aaaa"
        self.assertEqual(-1, str_str(haystack, needle))

    def test_longest_common_prefix(self):
        strs = ['flower', 'flow', 'flight']
        self.assertEqual('fl', longest_common_prefix(strs))

        strs = ['dog', 'racecar', 'car']
        self.assertEqual('', longest_common_prefix(strs))

        strs = ['carplay', 'racecar', 'car']
        self.assertEqual('', longest_common_prefix(strs))

    def test_reverse_string(self):
        self.assertEqual('olleh', reverse_string('hello'))
        self.assertEqual('', reverse_string(''))

    def test_array_pair_sum(self):
        self.assertEqual(4, array_pair_sum([1, 4, 3, 2]))

    def test_two_sum(self):
        self.assertEqual([1, 2], two_sum([2, 7, 11, 15], 9))

    def test_remove_element(self):
        self.assertEqual(2, remove_element([3, 2, 2, 3], 3))
        self.assertEqual(5, remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))

    def test_find_max_consecutive_ones(self):
        self.assertEqual(3, find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
        self.assertEqual(2, find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))

    def test_min_sub_array_len(self):
        self.assertEqual(2, min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))
        self.assertEqual(0, min_sub_array_len(100, []))

    def test_rotate_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(nums, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums)
        nums = [-1, -100, 3, 99]
        rotate(nums, 2)
        self.assertEqual([3, 99, -1, -100], nums)
        nums = []
        rotate(nums, 0)
        self.assertEqual([], nums)
        nums = [-1]
        rotate(nums, 2)
        self.assertEqual([-1], nums)

    def test_get_row(self):
        self.assertEqual([1], get_row(0))
        self.assertEqual([1, 1], get_row(1))
        self.assertEqual([1, 2, 1], get_row(2))
        self.assertEqual([1, 3, 3, 1], get_row(3))
        self.assertEqual([1, 4, 6, 4, 1], get_row(4))
