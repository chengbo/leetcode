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
