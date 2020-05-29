#### #1
# time exceed at case 199/200
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size==0: return 0
        
        memo = [0]
        maximum = -1
        for i in range(1,size):
            for k in range(i-1,-1,-1):
                maximum = max(maximum,prices[i]-prices[k])
            memo.append(maximum)
            
        return(max(memo))
    
#### #2 trial    
# Runtime: 64 ms, faster than 68.93% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy
    
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size==0: return 0
        
        memo = [0]
        maximum = -1
        for i in range(1,size):
            memo.append(max(0,prices[i]-(prices[i-1]-memo[i-1])))
        
        return(max(memo))
