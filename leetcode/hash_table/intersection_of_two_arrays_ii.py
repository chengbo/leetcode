def intersect(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
    return result


def intersect_ii(nums1, nums2):
    d = {}
    result = []

    for _, num in enumerate(nums1):
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1
    for _, num in enumerate(nums2):
        if num in d.keys() and d[num] > 0:
            result.append(num)
            d[num] -= 1

    return result
