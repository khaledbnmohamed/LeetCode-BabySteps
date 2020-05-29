#### #1
# time exceed at case 199/200

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
