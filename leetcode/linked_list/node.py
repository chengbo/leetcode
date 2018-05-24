class SinglyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val} -> {self.next}'
