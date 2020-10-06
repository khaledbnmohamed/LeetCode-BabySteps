
https://leetcode.com/problems/complement-of-base-10-integer/


#Runtime: 28 ms, faster than 78.44% of Python3 online submissions for Complement of Base 10 Integer.
#Memory Usage: 14.2 MB, less than 5.11% of Python3 online submissions for Complement of Base 10 Integer.





class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binaryN = list(bin(N)[2:])
        
        for i in range(len(binaryN)):
            if binaryN[i] == "1":
                binaryN[i] = "0"
            else:
                binaryN[i] = "1"

        return int(''.join(binaryN),2)
        
