class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curr = 1
        best = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                curr += 1
            elif diff != 0:
                curr = 1
            best = max(curr, best)
        return best