

#https://leetcode.com/problems/happy-number/submissions/

#Runtime: 32 ms, faster than 84.91% of Python3 online submissions for Happy Number.
#Memory Usage: 13.7 MB, less than 90.27% of Python3 online submissions for Happy Number.








class Solution:
    def isHappy(self, n: int) -> bool:
        if len(str(n)) == 1:
            if(n==1 or n == 7): return True;
            else: return False
        numbers_array = [int(i) for i in str(n)]
        total_count = 0
        for i in numbers_array:
            total_count += i**2
        return self.isHappy(total_count)
        
            
        
