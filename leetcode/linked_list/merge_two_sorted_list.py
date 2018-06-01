def merge(l1, l2):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    head = l1
    if l1.val > l2.val:
        head = l2
        l2 = l1
        l1 = head

    while l1.next is not None:
        if l1.next.val > l2.val:
            tmp = l1.next
            l1.next = l2
            l2 = tmp
        l1 = l1.next

    l1.next = l2
    return head


def merge_ii(l1, l2):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    if l1.val > l2.val:
        l2.next = merge(l1, l2.next)
        return l2

    l1.next = merge(l1.next, l2)
    return l1
