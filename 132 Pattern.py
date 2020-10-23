

#trivail solution , time exceeded

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        if len(nums) == 3:
            if nums[0] < nums[1] and nums[1] > nums[2] and nums[0] < nums[2]:
                return True
            else:
                return False
        for j in range(1,len(nums)-1):
            print(nums[j])
            for i in range(j-1,-1,-1):
                if nums[j] - nums[i] > 0:
                    for k in range(j,len(nums)):
                        if nums[j] - nums[k] > 0 and nums[k] - nums[i] > 0:
                            return True
        return False
