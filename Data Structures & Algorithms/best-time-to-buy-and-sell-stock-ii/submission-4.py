class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        final = 0
        curr = 0
        bigger = False
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit <= 0:
                if curr == right - 1:
                    final += prices[curr] - prices[left]
                left = right
                curr = left
            else:
                lastProfit = prices[curr] - prices[left]
                if lastProfit > profit:
                    left = right
                    final += lastProfit
                    curr = left
                else:
                    curr = right
                    bigger = True
        if bigger:
            final += prices[len(prices)-1] - prices[left]
        return final

