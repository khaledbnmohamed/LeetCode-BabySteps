# https://leetcode.com/problems/house-robber/submissions/
#top down recursive exceeding time limit trial #2
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.recuRob(nums,len(nums)-1)

    def recuRob(self, nums: List[int],size):
        if(size < 0):
            return 0
        return max(self.recuRob(nums,size-2)+nums[size],self.recuRob(nums,size-1))
