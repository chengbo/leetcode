def contains_duplicate(nums):
    if nums is None:
        return False
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False
