def intersection(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    intersection = set()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            intersection.add(nums1[i])
            i += 1
            j += 1
    return list(intersection)


def intersection_ii(nums1, nums2):
    s = set(nums1)
    intersection = set()
    for num in nums2:
        if num in s:
            intersection.add(num)
    return list(intersection)
