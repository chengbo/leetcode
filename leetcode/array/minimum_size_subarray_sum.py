def min_sub_array_len(s, nums):
    result = 0
    fast = slow = 0
    length = len(nums)
    min_length = length + 1
    while fast < length:
        result += nums[fast]
        while result >= s:
            min_length = min(min_length, fast - slow + 1)
            result -= nums[slow]
            slow += 1
        fast += 1
    return 0 if min_length == length + 1 else min_length
