def group_anagrams(strs):
    if strs is None:
        return []
    d = {}
    for _, s in enumerate(strs):
        chars = sorted(list(s))
        sorted_s = ''.join(chars)
        if sorted_s in d.keys():
            d[sorted_s].append(s)
        else:
            d[sorted_s] = [s]
    return list(d.values())
