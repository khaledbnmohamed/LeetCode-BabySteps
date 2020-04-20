# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        returned_index= 0
        for i in nums:
            if target > i:
                returned_index += 1

        return returned_index
        
#Runtime: 40 ms, faster than 98.12% of Python3 online submissions for Search Insert Position.
#Memory Usage: 14.4 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
