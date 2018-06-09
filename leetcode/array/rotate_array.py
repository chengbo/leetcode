def rotate(nums, k):
    length = len(nums)
    if length == 0:
        return nums

    k %= length

    nums[:] = nums[-k:] + nums[:-k]


def rotate_ii(nums, k):
    length = len(nums)
    if length == 0:
        return nums

    def reverse_array(array, f, t):
        while f < t:
            array[f], array[t] = array[t], array[f]
            f += 1
            t -= 1
    k %= length
    reverse_array(nums, 0, length - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, length - 1)


def rotate_iii(nums, k):
    if len(nums) == 0:
        return nums
    for _ in range(k):
        nums.insert(0, nums.pop())
