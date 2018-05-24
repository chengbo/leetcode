def is_palindrome(head):
    reversed_head = None
    fast = slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        tmp = reversed_head
        reversed_head = slow
        slow = slow.next
        reversed_head.next = tmp

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.val != reversed_head.val:
            return False
        slow = slow.next
        reversed_head = reversed_head.next

    return True


def is_palindrome_ii(head):
    fast = slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    if fast is not None:
        slow = slow.next

    reversed_head = current = slow
    while current is not None and current.next is not None:
        tmp = current.next
        current.next = current.next.next
        tmp.next = reversed_head
        reversed_head = tmp

    while reversed_head is not None:
        if reversed_head.val != head.val:
            return False
        reversed_head = reversed_head.next
        head = head.next

    return True
