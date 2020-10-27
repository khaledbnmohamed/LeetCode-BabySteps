#https://leetcode.com/problems/champagne-tower/




class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured < query_row: return float(0)
        
        res = [[0.0 for _ in range(i)] for i in range(1, query_row + 2)]
        res[0][0] = poured

        for i in range(query_row):
            for j in range(len(res[i])):
                if res[i][j] > 1:
                    res[i+1][j] += (res[i][j]-1) / 2.0
                    res[i+1][j+1] += (res[i][j]-1) / 2.0
        print(res)            
        if res[query_row][query_glass] <= 1:
            return res[query_row][query_glass]
        return 1
