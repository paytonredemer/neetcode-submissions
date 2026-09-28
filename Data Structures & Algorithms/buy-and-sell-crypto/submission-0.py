class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for p in prices:
            if p < low:
                low = p
            current_profit = p - low
            if current_profit > profit:
                profit = current_profit
        return profit