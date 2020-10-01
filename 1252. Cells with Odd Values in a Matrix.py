#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

# Runtime: 40 ms, faster than 90.15% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 14.1 MB, less than 12.87% of Python3 online submissions for Cells with Odd Values in a Matrix.

#time to answer 20 mins
#brute force
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for x in range(m)] for y in range(n)] 
        counter = 0
        for dimen in indices:
            row_number = dimen[0]
            coloumn_number = dimen[1]
            for i in range(m):
                matrix[row_number][i] +=1
            for j in range(n):
                matrix[j][coloumn_number] +=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    counter += 1
        return counter
