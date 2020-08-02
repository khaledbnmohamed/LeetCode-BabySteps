#https://leetcode.com/problems/coin-change/

#Runtime: 2392 ms, faster than 17.53% of Python3 online submissions for Coin Change.
#Memory Usage: 13.9 MB, less than 78.98% of Python3 online submissions for Coin Change.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins: return 1
        if amount == 0: return 0
        dp =[amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[-1] == amount +1:
            return -1 
        else:
            return dp[-1]


            
