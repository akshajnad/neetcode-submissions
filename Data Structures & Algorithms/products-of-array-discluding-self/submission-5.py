class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        prod = 1
        for i in range(len(nums)-1):
            prod *= nums[i]
            prefix.append(prod)
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            suffix.append(prod)
        suffix.reverse()
        return [prefix[i] * suffix[i] for i in range(len(nums))]