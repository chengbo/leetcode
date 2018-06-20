def contains_nearby_duplicate(nums, k):
    s = set()
    for i, num in enumerate(nums):
        if i > k:
            s.remove(nums[i - k - 1])
        if num in s:
            return True
        s.add(num)
    return False


def contains_nearby_duplicate_ii(nums, k):
    d = {}
    for i, num in enumerate(nums):
        if num in d.keys():
            for j in d[num]:
                if i - j <= k:
                    return True
            d[num].append(i)
        else:
            d[num] = [i]

    return False


def contains_nearby_duplicate_iii(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i <= k and nums[i] == nums[j]:
                return True
    return False
