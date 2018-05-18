import unittest
from leetcode.linked_list.my_linked_list import MyLinkedList


class TestLinkedList(unittest.TestCase):

    def test_my_linked_list(self):
        list = MyLinkedList()
        list.addAtHead(1)
        list.addAtIndex(1, 2)
        self.assertEqual(2, list.get(1))
        self.assertEqual(1, list.get(0))
        self.assertEqual(-1, list.get(2))

        list = MyLinkedList()
        self.assertEqual(-1, list.get(0))
        list.addAtIndex(1, 2)
        self.assertEqual(-1, list.get(0))
        self.assertEqual(-1, list.get(1))
        list.addAtIndex(0, 1)
        self.assertEqual(1, list.get(0))
        self.assertEqual(-1, list.get(1))
        list.addAtTail(3)
        self.assertEqual(1, list.get(0))
        self.assertEqual(3, list.get(1))
        list.deleteAtIndex(0)
        self.assertEqual(3, list.get(0))
        list.deleteAtIndex(2)
        self.assertEqual(3, list.get(0))
        list.deleteAtIndex(0)
        self.assertEqual(-1, list.get(0))
