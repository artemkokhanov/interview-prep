def top_k_frequent_elements(nums, k):
    count = {}
    # len(nums) + 1 because each number in the nums array will occur at least once, the 0 count index will not be filled
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

# Example:
# [1,1,1,2,2,3]
# count = {1: 3, 2: 2, 3: 1}
#         0    1    2    3   4   5   6
# freq = [[], [3], [2], [1], [], [], []]
