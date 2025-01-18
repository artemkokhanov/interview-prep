def top_k_frequent_elements(nums, k):
    # index is the frequency:                                0    1    2    3    4    5    6
    # value is list of elements that match the frequency:  [[ ], [3], [2], [1], [ ], [ ], [ ]]
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for num, c in count.items():
        freq[c].append(num)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for j in freq[i]:
            result.append(j)

            if len(result) == k:
                return result
