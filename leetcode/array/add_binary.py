def add_binary(a, b):
    a, b = list(a), list(b)
    carry = 0
    result = []
    while len(a) > 0 or len(b) > 0 or carry != 0:
        aa = int(a.pop()) if len(a) > 0 else 0
        bb = int(b.pop()) if len(b) > 0 else 0
        carry, tmp = divmod(carry + aa + bb, 2)
        result.append(str(tmp))

    return ''.join(result[::-1])


def add_binary_ii(a, b):
    a = int(a, 2)
    b = int(b, 2)
    return '{0:b}'.format(a + b)
