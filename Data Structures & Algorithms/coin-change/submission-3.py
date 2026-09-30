
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def check(curr, num):
            if curr == 0:
                nums.append(num)
                return
            elif curr < 0:
                return
            if curr in cache and cache[curr] <= num:
                return
            cache[curr] = num
            for coin in coins:
                check(curr - coin, num + 1)
        nums = []
        cache = {}
        check(amount, 0)
        return -1 if not nums else min(nums)
        
        