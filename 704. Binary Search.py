#https://leetcode.com/problems/binary-search


#Runtime: 236 ms, faster than 88.43% of Python3 online submissions for Binary Search.
#Memory Usage: 15.2 MB, less than 30.12% of Python3 online submissions for Binary Search.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
    
        if (target < nums[0] or target > nums[len(nums)-1]): return -1
        start = 0
        end = len(nums)-1
        
        while end - start !=  0:
            bisector = ((end-start)//2) +start
            if target == nums[bisector]: return bisector
            
            if target < nums[bisector]:
                end = bisector
            else:
                start =  bisector +1
        if target == nums[end]: return end
        return -1
