def remove_nth_from_end(head, n):
    if head is None:
        return None

    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
