def has_cycle(head):
    try:
        fast = head.next
        slow = head
        while fast is not slow:
            fast = fast.next.next
            slow = slow.next
        return True
    except AttributeError:
        return False


def has_cycle_ii(head):
    try:
        fast = head.next
        slow = head
        while fast is not slow:
            fast = fast.next.next
            slow = slow.next
        fast = head
        slow = slow.next
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
    except AttributeError:
        return None
