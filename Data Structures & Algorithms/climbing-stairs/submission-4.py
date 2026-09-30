from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def backtrack(step):
            if step > n:
                return 0
            if step == n:
                return 1
            return backtrack(step + 1) + backtrack(step + 2)

        return backtrack(0)