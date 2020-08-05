# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
#Runtime: 64 ms, faster than 82.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 15 MB, less than 85.41% of Python3 online submissions for Best Time to Buy and Sell Stock.
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0: return 0
        dp = [0]
        for i in range(1,size):
            dp.append(max(0,prices[i]-(prices[i-1]-dp[i-1])))
            
        return max(dp)
