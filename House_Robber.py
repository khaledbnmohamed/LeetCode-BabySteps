# https://leetcode.com/problems/house-robber/submissions/
#top down recursive with a memory to prevent repeating myself trial #2
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
