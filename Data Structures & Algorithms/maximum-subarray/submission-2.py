class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float("-inf")
        curr = float("-inf")
        for num in nums:
            curr = max(curr + num, num)
            best = max(best, curr)
        return best