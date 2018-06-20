def first_uniq_char(s):
    d = {}
    for i, c in enumerate(s):
        count = d.get(c, 0)
        count += 1
        d[c] = count
    for i, c in enumerate(s):
        if d[c] == 1:
            return i

    return -1
