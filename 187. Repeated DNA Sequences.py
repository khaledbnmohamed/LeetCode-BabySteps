#https://leetcode.com/problems/repeated-dna-sequences/



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
