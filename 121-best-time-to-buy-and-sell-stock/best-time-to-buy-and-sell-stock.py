class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        best = 0
        while sell<len(prices):
            current = prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                best = max(best,current)
            else:
                buy = sell
            sell+=1
        return best