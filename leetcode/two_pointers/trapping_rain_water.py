from typing import List


# runs in O(n) time where n is the length of the input list
def trap(height: List[int]) -> int:
    if not height: return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]  # this will never be negative because we are updating leftMax before
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res
