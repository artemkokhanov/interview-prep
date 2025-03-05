# Q: Find a non-empty subarray with the largest sum

# Kadane's Algorithm: O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


# Q: Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# I.e., same question as above but we must return the indices of the beginning and end of the subarray
# Sliding window variation of Kadane's: O(n)
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]
