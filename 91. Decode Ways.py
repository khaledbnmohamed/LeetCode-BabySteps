#https://leetcode.com/problems/decode-ways/

#my personal updated solution :

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return 1
        size = len(s)
        arr= [1] * (size+1)
        for i in range(2,size+1):
            if s[i-1] == '0':
                if (s[i-2] != '1' and s[i-2] != '2'): return 0
                else:
                    arr[i] = arr[i-2]
            else:
                number = int(s[i-2]+s[i-1])
                if 10 <= number <= 26:
                    arr[i] = arr[i-1] +arr[i-2]
                else:
                    arr[i] = arr[i-1]
        return arr[-1]
    



class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return 1

        size = len(s)
        arr= [1] * (size+1)
        for i in range(2,size+1):
            if s[i-1] == '0':
                if 1 <= int(s[i-2]) <= 2:
                    arr[i] = arr[i-2]
                else:
                    arr[i] = 0
            else:
                if 10 <= int(s[i-2]+s[i-1]) <= 26:
                    arr[i] = arr[i-1] +arr[i-2]
                else:
                    arr[i] = arr[i-1]

                
        return arr[-1]
