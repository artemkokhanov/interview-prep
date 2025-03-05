# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # two-pointer solution (l tracks the position where the next distinct element should go, r is scanning through the array):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]  # stores the newly found unique element at the next available position (l) in the array in-place
                l += 1
        return l  # the number of unique elements in nums

# https://www.youtube.com/watch?v=DEJAZBq0FDA
