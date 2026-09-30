class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                curr = 1
                while num + 1 in nums:
                    curr += 1
                    num += 1
                best = max(curr, best)
        return best
        
        
        
        
        
        
        """if len(nums) == 0:
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
        return best"""