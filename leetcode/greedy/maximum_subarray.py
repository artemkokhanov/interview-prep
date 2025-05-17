from typing import List


# Kadane's Algorithm
def maxSubArray(nums: List[int]) -> int:
    maxSum = nums[0]
    curSum = 0

    for num in nums:
        curSum = max(curSum, 0)
        curSum += num
        maxSum = max(maxSum, curSum)
    return maxSum
