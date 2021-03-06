# https://leetcode.com/problems/house-robber/submissions/
# Based on solution :  https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
# Steps :
# 1) Think about recursive relation
# 2) try to apply it 
# 3) optimize it by adding a memory to save repeated values

############################################
# trial # 2
# top down recursive with a memory to prevent repeating myself 
############################################
# Runtime: 24 ms, faster than 92.54% of Python3 online submissions for House Robber.
# Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.recuRob(nums,len(nums)-1,memo)

    def recuRob(self, nums: List[int],size,memo):
        if(size < 0):
            return 0
        if(memo[size] >= 0):
            return (memo[size])
        result = max(self.recuRob(nums,size-2,memo)+nums[size],self.recuRob(nums,size-1,memo))
        memo[size] = result
        return result

############################################
# trial # 3
# itertaive DP following the dp template
############################################
# Runtime: 28 ms, faster than 74.79% of Python3 online submissions for House Robber.
# Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size==0: return 0
        memo = [0]
        memo.append(nums[0])
            
        for i in range(1,size):
            memo.append(max(memo[i],memo[i-1]+nums[i]))
            
        return(memo[size])
