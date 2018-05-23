def reverse_list(head):
    try:
        current_head = head
        while True:
            head_next = head.next
            head.next = head_next.next
            head_next.next = current_head
            current_head = head_next
    except AttributeError:
        return current_head
