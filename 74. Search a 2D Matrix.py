#https://leetcode.com/problems/search-a-2d-matrix/




#2nd trial with checkiing start and end of each row
# Runtime: 40 ms, faster than 96.71% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.3 MB, less than 85.38% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                for j in range(n):
                    if matrix[i][j] == target: return True
                return False
        return False







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
