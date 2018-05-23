import unittest
from leetcode.linked_list.cycle import has_cycle, has_cycle_ii
from leetcode.linked_list.intersection import get_intersection_node
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

    def test_has_cycle_ii(self):
        head = SinglyListNode(1)
        head.next = SinglyListNode(2)
        head.next.next = SinglyListNode(3)
        self.assertEqual(None, has_cycle_ii(head))

        head = SinglyListNode(1)
        head.next = SinglyListNode(2)
        node = SinglyListNode(3)
        head.next.next = node
        head.next.next.next = SinglyListNode(4)
        head.next.next.next.next = SinglyListNode(5)
        head.next.next.next.next.next = node
        self.assertEqual(node, has_cycle_ii(head))

        head = SinglyListNode(1)
        head.next = SinglyListNode(2)
        node = SinglyListNode(3)
        head.next.next = node
        head.next.next.next = SinglyListNode(4)
        head.next.next.next.next = SinglyListNode(5)
        head.next.next.next.next.next = SinglyListNode(6)
        head.next.next.next.next.next.next = node
        self.assertEqual(node, has_cycle_ii(head))

    def test_get_intersection_node(self):
        head_a = SinglyListNode(1)
        head_a.next = SinglyListNode(2)
        head_a.next.next = SinglyListNode(3)
        head_b = SinglyListNode(1)
        head_b.next = SinglyListNode(2)
        head_b.next.next = SinglyListNode(3)
        self.assertIsNone(get_intersection_node(head_a, head_b))

        intersection = SinglyListNode(1)
        intersection.next = SinglyListNode(2)
        head_a = SinglyListNode(1)
        head_a.next = intersection
        head_b = SinglyListNode(1)
        head_b.next = SinglyListNode(2)
        head_b.next.next = intersection
        self.assertEqual(intersection, get_intersection_node(head_a, head_b))