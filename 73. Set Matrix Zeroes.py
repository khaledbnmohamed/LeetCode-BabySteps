#Runtime: 132 ms, faster than 64.14% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15 MB, less than 74.11% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows= defaultdict(int)
        cols = defaultdict(int)
        # k -> coord[0]  rows
        for k in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[k][m] == 0:
                    rows[k] = k
                    cols[m] = m
           
        for k in rows:
            for i in range(len(matrix[0])):
                matrix[rows[k]][i] = 0
        for m in cols:
            for j in range(len(matrix)):
                matrix[j][cols[m]] = 0

