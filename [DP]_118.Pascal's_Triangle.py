# https://leetcode.com/problems/pascals-triangle/

# Runtime: 28 ms, faster than 71.47% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.6 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==0 : return []
        if numRows ==1 : return [[1]]

        memo= [[1]]
        memo.append([1,1])
        
        for i in range(2,numRows):
            new_row = [1] * (i+1)
            
            for k in range(1,i):
                new_row[k]= memo[i-1][k]+memo[i-1][k-1]
            
            memo.append(new_row)
                    
        return memo
        
