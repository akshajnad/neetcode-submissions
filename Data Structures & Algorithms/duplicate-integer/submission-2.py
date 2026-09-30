class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        return False