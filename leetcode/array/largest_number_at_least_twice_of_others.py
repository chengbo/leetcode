def dominant_index(nums):
    largest = sec_largest = -1
    index = -1
    for i, num in enumerate(nums):
        if num > largest:
            sec_largest = largest
            largest = num
            index = i
        elif num > sec_largest:
            sec_largest = num
    if largest >= sec_largest * 2:
        return index
    return -1
