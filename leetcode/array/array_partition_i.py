def array_pair_sum(nums):
    if len(nums) == 0:
        return 0
    nums = sorted(nums)
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result
