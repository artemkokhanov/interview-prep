# https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

# https://www.youtube.com/watch?v=68isPRHgcFQ
