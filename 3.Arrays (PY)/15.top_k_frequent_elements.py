# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     freqs = dict[int, list[int]]()

#     for num in nums:
#         if num in freqs:
#             freqs[num][0] += 1
#         else:
#             freqs[num] = [1, num]

#     arr = sorted(freqs.values(), reverse=True)[:k]
#     result = [0] * k
#     for i in range(k):
#         result[i] = arr[i][1]

#     return result

# bucket sort solution -> tc - O(n), sc - O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq: dict[int, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result = [0] * k
    found = 0
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            result[found] = n
            found += 1
            if found >= k:
                return result
    return result


print(topKFrequent([1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3, 1, 3, 2], 2))
