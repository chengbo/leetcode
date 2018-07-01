import collections


def four_sum_count(a, b, c, d):
    dic = collections.defaultdict(int)

    for i in range(len(a)):
        for j in range(len(b)):
            dic[a[i] + b[j]] += 1

    count = 0
    for i in range(len(c)):
        for j in range(len(d)):
            count += dic[0 - c[i] - d[j]]

    return count
