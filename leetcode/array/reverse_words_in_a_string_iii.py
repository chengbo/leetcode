def reverse_words(s):
    s = list(s)

    def reverse(f, t):
        while f < t:
            s[f], s[t] = s[t], s[f]
            f += 1
            t -= 1

    f = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse(f, i - 1)
            f = i + 1

    reverse(f, len(s) - 1)
    return ''.join(s)


def reverse_words_ii(s):
    return ' '.join(s.split()[::-1])[::-1]
