class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        product = prefix[0]
        for i in range(1, len(nums)):
            product *= nums[i-1]
            prefix.append(product)
        product = suffix[0]
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]            
            suffix.append(product)
        suffix.reverse()
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums