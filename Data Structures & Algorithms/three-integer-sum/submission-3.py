class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        result = list(result)
        for i in range(len(result)):
            result[i] = list(result[i])

        return result