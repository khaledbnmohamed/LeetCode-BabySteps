#https://leetcode.com/problems/buddy-strings/



#Runtime: 32 ms, faster than 76.37% of Python3 online submissions for Buddy Strings.
#Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Buddy Strings.




class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not A or not B: return False
        if len(A) != len(B): return False
        stack = []
        counter = 0
        if A == B:
            if (len(A) - len(''.join(set(A)))) < 1 :
                return False
            else:
                return True
        if len(A) == 2 and A == B: return True
        for i in range(len(A)):
            if A[i] != B[i]:
                if(not stack):
                    stack.append(A[i])
                    stack.append(B[i])

                elif (stack[-1] == A[i] and stack[-2] ==B[i]):
                    stack.pop()
                    stack.pop()

                    counter += 1
                else:
                    stack.append(A[i])
        if  not stack and counter == 1 : return True
        return False
