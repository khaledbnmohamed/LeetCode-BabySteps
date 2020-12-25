#https://leetcode.com/problems/diagonal-traverse/submissions/

#Runtime: 192 ms, faster than 67.79% of Python3 online submissions for Diagonal Traverse.
#Memory Usage: 17.4 MB, less than 6.73% of Python3 online submissions for Diagonal Traverse.

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        levels = defaultdict(list)
        for i,j in (product(range(m),range(n))):
            levels[i+j].append(matrix[i][j])
            
        result = []
        for level in range(len(levels)):
            result += levels[level][::level%2*2-1]
        return result
