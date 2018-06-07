def find_max_consecutive_ones(nums):
    maximum = 0
    j = 0
    for i in range(len(nums)):
        if nums[i] != 1:
            maximum = max(maximum, i - j)
            j = i + 1
    return max(maximum, len(nums) - j)
