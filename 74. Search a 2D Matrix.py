#https://leetcode.com/problems/search-a-2d-matrix/



















# brute force solution
# Runtime: 44 ms, faster than 92.85% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.5 MB, less than 85.38% of Python3 online submissions for Search a 2D Matrix.




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target: return True
        return False
