def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_ii(nums):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    for key, val in d.items():
        if val != 2:
            return key
