https://leetcode.com/problems/the-kth-factor-of-n/

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
            
