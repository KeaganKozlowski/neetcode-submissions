class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, n = 0, len(prices)
        for i in range(n):
            for j in range(i,n):
                best = max(best, prices[j] - prices[i])
        return best
