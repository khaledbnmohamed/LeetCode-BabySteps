#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = []
        sum = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    sum = sum * nums[j]
            output_array.append(sum)
            sum = 1
        return output_array
                    
