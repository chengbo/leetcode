def find_pivot_index(nums):
    left, right = 0, sum(nums)

    for i, num in enumerate(nums):
        right -= num
        if left == right:
            return i
        left += num

    return -1
