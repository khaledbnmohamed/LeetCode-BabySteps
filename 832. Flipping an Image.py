#https://leetcode.com/problems/flipping-an-image/

#Runtime: 48 ms, faster than 79.68% of Python3 online submissions for Flipping an Image.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Flipping an Image.







class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        stack = []
        size = len(A)
        middle = floor(size / 2)
        for row in A:
            for j in row:
                stack.append(j)
            i = 0    
            while stack:
                row[i] = int(not(stack.pop()))
                i += 1
        return A
