#https://leetcode.com/problems/search-a-2d-matrix/

























class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target: return True
        return False
