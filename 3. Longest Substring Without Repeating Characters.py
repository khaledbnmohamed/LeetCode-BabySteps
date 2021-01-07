#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Runtime: 76 ms, faster than 37.62% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Memory Usage: 14.3 MB, less than 49.08% of Python3 online submissions for Longest Substring Without Repeating Character


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) ==1: return 1
        dict = {}
        start = 1
        end = 0
        max_sub = -1
        
        for i in range(0,len(s)):
            if s[i] not in dict:
                end += 1
                dict[s[i]] = i
            else:
                max_sub = max(max_sub,(end-start)+1)
                start = max(start,dict[s[i]]+1)
                end = i
                dict[s[i]] = i
        last_sub = min(len(s),(end+1)-start)
        return max(max_sub,last_sub)            
