class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            while profit <= 0 and l < r:
                l += 1
                profit = prices[r] - prices[l]
            best = max(profit, best)
        return best