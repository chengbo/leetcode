def reverse_string(s):
    if s is None:
        return None
    head, end = 0, len(s) - 1
    s = list(s)
    while head < end:
        s[head], s[end] = s[end], s[head]
        head += 1
        end -= 1
    return ''.join(s)
