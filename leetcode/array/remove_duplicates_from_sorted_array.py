def remove_duplicates(nums):
    length = len(nums)
    if length == 0:
        return 0
    current = 0
    for i in range(1, length):
        if nums[i] != nums[current]:
            current += 1
            nums[current] = nums[i]
    return current + 1
