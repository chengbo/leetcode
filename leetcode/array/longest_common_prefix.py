def longest_common_prefix(strs):
    if strs is None or len(strs) == 0:
        return ''
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
    return prefix
