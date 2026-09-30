class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
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
                    result.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return [list(i) for i in set(result)]
                