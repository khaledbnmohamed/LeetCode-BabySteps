#https://leetcode.com/problems/reach-a-number/submissions/


#Runtime: 28 ms, faster than 91.95% of Python3 online submissions for Reach a Number.
#Memory Usage: 14.4 MB, less than 6.71% of Python3 online submissions for Reach a Number.


class Solution:
    def reachNumber(self, target: int) -> int:
        a = 1
        b = 1
        c= -(abs(target)*2)
        
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        
        bound = math.ceil(min(abs(x1),abs(x2)))

        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1

        
        return  bound
