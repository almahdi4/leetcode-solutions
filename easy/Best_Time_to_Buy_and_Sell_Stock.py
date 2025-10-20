class Solution:
# 121. Best Time to Buy and Sell Stock
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Track the minimum price so far and compute the best profit at each step.
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        curr_profit = 10**5
        for price in prices:
            if price < curr_profit:
                curr_profit = price
            elif price - curr_profit > max_profit:
                max_profit = price - curr_profit
        return max_profit