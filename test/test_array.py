import unittest
from leetcode.array.find_pivot_index import find_pivot_index


class TestArray(unittest.TestCase):

    def test_find_pivot_index(self):
        array = [1, 7, 3, 6, 5, 6]
        self.assertEqual(3, find_pivot_index(array))

        array = [1, 2, 3]
        self.assertEqual(-1, find_pivot_index(array))
