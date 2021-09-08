# https://leetcode.com/problems/container-with-most-water/submissions/

#Runtime: 752 ms, faster than 56.07% of Python3 online submissions for Container With Most Water.
#Memory Usage: 27.5 MB, less than 57.14% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) -1
        
        max_val= -1
        
        while l < r:
            max_val = max(max_val,min(height[l],height[r])* (r-l))
            if  height[l]< height[r]:
                l +=1 
            else:
                r -=1 
        return max_val
