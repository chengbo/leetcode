def num_jewels_in_stones(j, s):
    d = set(j)
    count = 0
    for _, c in enumerate(s):
        if c in d:
            count += 1
    return count
