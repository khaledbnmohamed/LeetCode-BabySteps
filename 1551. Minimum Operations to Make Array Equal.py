


#Runtime: 72 ms, faster than 55.73% of Python3 online submissions for Minimum Operations to Make Array Equal.
#Memory Usage: 14.1 MB, less than 12.13% of Python3 online submissions for Minimum Operations to Make Array Equal.







class Solution:
    def minOperations(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        counter = 0
        if (n%2 ==0):
            valueToStart = n/2 -1
        else:
            valueToStart = n//2
        valueToStart = 2*valueToStart +1
        while valueToStart > 0:
            counter += n-valueToStart
            valueToStart -= 2
        return int(counter)
