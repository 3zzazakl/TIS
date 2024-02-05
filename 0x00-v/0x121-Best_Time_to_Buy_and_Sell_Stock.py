#!/usr/bin/python3
"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    BigO: O(n)
"""

class Solution(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return (0)

        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, (prices[i] - min_price))
        return (max_profit)


leetcode = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(leetcode.maxProfit(prices1))
print(leetcode.maxProfit(prices2))
