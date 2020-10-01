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
#2nd trial
# Runtime: 36 ms, faster than 96.33% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Memory Usage: 14.1 MB, less than 11.90% of Python3 online submissions for Cells with Odd Values in a Matrix.

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        x, y = [0] * n, [0] * m
        for i in indices:
            x[i[0]] += 1
            y[i[1]] += 1
        #https://stackoverflow.com/a/20639246/5627553
        
        #https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/discuss/813726/Short-sweet-efficient-Python-wexplanation.
        return sum([1 for j in y for i in x if (j+i) % 2])
