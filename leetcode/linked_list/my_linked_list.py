from leetcode.linked_list.node import SinglyListNode


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            i = i+1
            current = current.next

        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node
        of the linked list.
        :type val: int
        :rtype: void
        """
        node = SinglyListNode(val)
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = SinglyListNode(val)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        node = SinglyListNode(val)
        if self.head is None:
            if index == 0:
                self.head = node
            return
        current = self.head
        i = 1
        while current.next is not None:
            if i == index:
                node.next = current.next
                current.next = node
                return
            i = i+1
            current = current.next
        if i == index:
            current.next = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        i = 1
        while current.next is not None:
            if i == index:
                current.next = current.next.next
                return
            i = i+1
            current = current.next
