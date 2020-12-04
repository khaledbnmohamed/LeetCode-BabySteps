#https://leetcode.com/problems/the-kth-factor-of-n/
#Runtime: 36 ms, faster than 25.30% of Python3 online submissions for The kth Factor of n.
#Memory Usage: 14.1 MB, less than 35.66% of Python3 online submissions for The kth Factor of n.
    
    
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        increase = 0
        
        for i in range(1,n+1):
            if(len(factors) == k): break
            if (n % (i +1) == 0):
                factors.append((i+1))
        if (len(factors) == k):
            return factors[-1]
        else:
            return -1
            
