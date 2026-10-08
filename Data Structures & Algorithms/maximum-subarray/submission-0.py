class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = nums[0]
        curr = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            if prefix <= 0:
                prefix = 0
                curr = 0
            curr += nums[i]
            prefix += nums[i]
            best = max(curr, best)
        return best