def str_str(haystack, needle):
    i = 0
    while True:
        j = 0
        while True:
            if j == len(needle):
                return i
            if i + j == len(haystack):
                return -1
            if haystack[i + j] != needle[j]:
                break
            j += 1
        i += 1
