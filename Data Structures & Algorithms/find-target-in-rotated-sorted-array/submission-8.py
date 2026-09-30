class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            #left
            if nums[m] >= nums[l]:
                #less than in left
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #greater than in right
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

        """l = 0
        h = len(nums)-1
        pivot = -1
        while l <= h:
            m = (l+h)//2
            if nums[m-1] > nums[m]:
                pivot = m
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                h = m - 1
        offset = 0
        if pivot == -1:
            pivot = 0 if nums[0] < nums[-1] else len(nums)-1 
        if target > nums[0]:
            nums = nums[:pivot]
        elif target < nums[0]:
            offset = pivot
            nums = nums[pivot:]
        else:
            return 0
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                return m + offset
        return -1"""