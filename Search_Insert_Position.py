# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
            return index
        except:
            if (target > nums[len(nums)-1]):
                return len(nums)
            elif(target <nums[0]):
                return 0
            else:
                num_at= self.recursiveSearch(nums,target)
                index = nums.index(num_at) +1 
                return index
    
    def recursiveSearch(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if( size == 1 ):
            return nums[0]
        if(target < nums[size//2]):
            return self.recursiveSearch(nums[0:size//2],target)
        else:
            return self.recursiveSearch(nums[size//2:size],target)

#Runtime: 40 ms, faster than 98.12% of Python3 online submissions for Search Insert Position.
#Memory Usage: 14.4 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
