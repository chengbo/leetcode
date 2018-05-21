import unittest
from leetcode.linked_list.cycle import has_cycle
from leetcode.linked_list.my_linked_list import MyLinkedList
from leetcode.linked_list.node import SinglyListNode


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

    def test_has_cycle(self):
        head = SinglyListNode(1)
        head.next = SinglyListNode(2)
        head.next.next = SinglyListNode(3)
        self.assertFalse(has_cycle(head))

        head = SinglyListNode(1)
        head.next = SinglyListNode(2)
        node = SinglyListNode(3)
        head.next.next = node
        head.next.next.next = SinglyListNode(4)
        head.next.next.next.next = SinglyListNode(5)
        head.next.next.next.next.next = node
        self.assertTrue(has_cycle(head))
