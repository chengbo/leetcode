def get_intersection_node(head_a, head_b):
    a, b = head_a, head_b

    while a is not b:
        a = head_b if a is None else a.next
        b = head_a if b is None else b.next

    return a
