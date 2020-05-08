# https://leetcode.com/problems/climbing-stairs/
#Following the DP tempalte

# Runtime: 24 ms, faster than 90.34% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs




class Solution:
    def climbStairs(self, n: int) -> int:
        
        if (n < 4 ): 
            return n
        
        memo = [1]
        memo.append(2)
        memo.append(3)
        
        for i in range(3,n):
            memo.append(memo[i-1]+memo[i-2])
        
        return memo.pop()
