class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0
        water = 0
        maxl = 0
        maxr = 0
        l = 0
        r = len(height) - 1

        while l < r:
            add = 0
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                add = maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                add = maxr - height[r]
                r -= 1
            water += add
            
        return water