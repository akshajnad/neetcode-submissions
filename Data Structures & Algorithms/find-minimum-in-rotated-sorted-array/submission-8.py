class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m-1] > nums[m]:
                return nums[m]
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                h = m - 1
        return nums[0] if nums[0] < nums[-1] else nums[-1]    