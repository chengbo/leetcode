def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def plus_one_ii(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        if carry == 0:
            return digits
        carry, digits[i] = divmod(digits[i] + carry, 10)
    if carry > 0:
        return [carry] + digits
    return digits
