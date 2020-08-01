#https://leetcode.com/problems/two-sum/

#Runtime: 1412 ms, faster than 21.24% of Python3 online submissions for Two Sum.
#Memory Usage: 14.9 MB, less than 74.32% of Python3 online submissions for Two Sum.
#

# 1st attp
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            stored_val = nums[i]
            other_value = target- stored_val
            nums[i] = "#"
            try:
                y = nums.index(other_value)
                return [y,i]
            except:
                nums[i] = stored_val

