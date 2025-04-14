from typing import List


def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0  # rob2 is the last house robbed, rob1 is the house(s) robbed before that

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
    # we return rob2 because by the time we get to the end of nums, rob2 will be equal to the last value,
    # meaning it will be the max we can rob from the entire neighborhood of houses
