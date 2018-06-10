def reverse_words(s):
    fast = slow = 0
    in_word = False
    array = []
    for i in range(len(s)):
        if s[i] == ' ':
            if in_word:
                array.append(s[slow:fast + 1])
            else:
                fast = slow = i
            in_word = False
        else:
            if in_word:
                fast = i
            else:
                fast = slow = i
            in_word = True

    if in_word:
        array.append(s[slow:fast + 1])

    return ' '.join(reversed(array))
