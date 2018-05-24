def odd_even_list(head):
    if head is None:
        return head

    odd = head
    even = even_head = head.next

    while even is not None and even.next is not None:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head

    return head
