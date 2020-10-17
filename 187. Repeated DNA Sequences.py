#https://leetcode.com/problems/repeated-dna-sequences/






# 1st trial , brute force solution
# Runtime: 64 ms, faster than 68.81% of Python3 online submissions for Repeated DNA Sequences.
# Memory Usage: 27.8 MB, less than 5.88% of Python3 online submissions for Repeated DNA Sequences.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = {}
        for i in range(len(s)):
            if s[i:i+10] in dict:
                dict[s[i:i+10]] += 1
            else:
                dict[s[i:i+10]] = 1
        keys = []
        for key, value in dict.items():
            if value > 1:
                keys.append(key)
        return keys
