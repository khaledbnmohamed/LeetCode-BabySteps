#https://leetcode.com/problems/stone-game-iv/

# Runtime: 2900 ms, faster than 33.33% of Python3 online submissions for Stone Game IV.
# Memory Usage: 14.8 MB, less than 6.86% of Python3 online submissions for Stone Game IV.

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n == (math.isqrt(n) ** 2) or  n == 1 or n == 3: return True
        
        if n < 4: return False

        dp = [False] * (n+1)
        dp[1]=True
        dp[2]= False
        
        for i in range(3,len(dp)):
            if i == (math.isqrt(i) ** 2):
                dp[i] = True
            else:
                number = 1
                power = 1 
                while power < i:
                    if dp[power] != dp[i-power] :
                        dp[i] = True
                        power = i
                    else:
                        number = number +1 
                        power = (number) ** 2
                
        return dp[-1]
