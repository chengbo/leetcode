def length_of_longest_substring(s):
    d = {}
    longest = j = 0

    for i, c in enumerate(s):
        if c in d.keys():
            j = max(j, d[c] + 1)
        d[c] = i
        longest = max(longest, i - j + 1)

    return longest
