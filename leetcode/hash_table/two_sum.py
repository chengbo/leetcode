def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        tmp = target - num
        if tmp in d and i != d[tmp]:
            return [d[tmp], i]
        d[num] = i


def two_sum_ii(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
