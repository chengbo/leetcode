def move_zeroes(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1
