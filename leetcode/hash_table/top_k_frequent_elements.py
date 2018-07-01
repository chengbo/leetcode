import collections


def top_k_frequent(nums, k):
    d = collections.defaultdict(int)
    for _, num in enumerate(nums):
        d[num] += 1

    return [
        k for k, _ in sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:k]
    ]
