class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        def rob(arr):
            dp = [arr[0], max(arr[0], arr[1])]
            for i in range(2, len(arr)):
                dp.append(max(arr[i] + dp[i-2], dp[i - 1]))
            return dp[-1]
        return max(rob(nums[:len(nums)-1]), rob(nums[1:]))