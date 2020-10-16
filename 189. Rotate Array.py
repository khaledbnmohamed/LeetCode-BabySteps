#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1: return 
        k = k % size
        temp = nums[0:size-k]
        while(len(nums)> k):
            nums.pop(0)
        nums.extend(temp)
