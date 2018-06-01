from leetcode.linked_list.node import SinglyListNode


def add_two_numbers(l1, l2):
    dummy = node = SinglyListNode(0)
    carry = 0

    while l1 is not None or l2 is not None or carry > 0:
        v1 = v2 = 0
        if l1 is not None:
            v1 = l1.val
            l1 = l1.next
        if l2 is not None:
            v2 = l2.val
            l2 = l2.next
        carry, v = divmod(v1 + v2 + carry, 10)
        node.next = SinglyListNode(v)
        node = node.next

    return dummy.next
