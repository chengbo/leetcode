def is_isomorphic(s, t):
    m1 = [-1] * 256
    m2 = [-1] * 256
    for i in range(len(s)):
        a, b = ord(s[i]), ord(t[i])
        if m1[a] != m2[b]:
            return False
        m1[a] = m2[b] = i

    return True


def is_isomorphic_ii(s, t):
    def check(a, b):
        mapping = {}
        for i in range(len(a)):
            if a[i] in mapping.keys() and b[i] != mapping[a[i]]:
                return False
            mapping[a[i]] = b[i]
        return True

    if not check(s, t):
        return False
    return check(t, s)
