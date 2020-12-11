#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return 
        counter = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                counter += 1
                if counter > 1:
                    nums.pop(i-1)
                    counter -= 1
            else:
                counter = 0
