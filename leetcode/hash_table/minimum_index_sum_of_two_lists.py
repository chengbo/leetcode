def find_restaurant(list1, list2):
    d1 = {}
    for i, v in enumerate(list1):
        d1[v] = i
    result = []
    min_sum = len(list1) + len(list2) - 2
    for i, v in enumerate(list2):
        if v in d1.keys():
            index_sum = d1[v] + i
            if index_sum < min_sum:
                min_sum = index_sum
                result.clear()
                result.append(v)
            elif index_sum == min_sum:
                result.append(v)

    return result
