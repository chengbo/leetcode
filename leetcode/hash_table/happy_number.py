def is_happy(n):
    def digit_square_sum(n):
        result = 0
        quotient = n
        while quotient > 0:
            quotient, remainder = divmod(quotient, 10)
            result += remainder**2
        return result
    fast = slow = n
    while True:
        fast = digit_square_sum(fast)
        fast = digit_square_sum(fast)
        slow = digit_square_sum(slow)
        if fast == 1:
            return True
        if fast == slow:
            return False


def is_happy_ii(n):
    result = n
    seen = set()
    while result != 1:
        if result in seen:
            return False
        seen.add(result)
        tmp = 0
        quotient = result
        while quotient > 0:
            quotient, remainder = divmod(quotient, 10)
            tmp += remainder**2
        result = tmp
        quotient = tmp

    return True
