class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        dp =[ [0, False]*1 for i in range(len(nums)+1)]
    
        dp[1] = [nums[0],True]


        dp[2] = [max(nums[0],nums[1]),nums[0] > nums[1]]

        

        if(len(nums) == 3): return dp[-2][0]
        if(len(nums) == 2): return dp[-1][0]

        fromZeroPosition = False

        for i in range(3,len(nums)+1):
            dp[i][0] =max(dp[i-1][0],dp[i-2][0]+nums[i-1])

            if(dp[i-1][0] < dp[i-2][0]+nums[i-1]):
                dp[i][1] = dp[i-2][1]
            else:
                 dp[i][1] = dp[i-1][1]
            
                    
        i = len(nums)
        if(dp[i-1][0] < dp[i-2][0]+nums[i-1]):
            endIncluded = True
        else:
            endIncluded = False
            
        print(dp)
        print(endIncluded)
        if(dp[-1][1] and endIncluded):
            return max(dp[-1][0]-nums[0],dp[-2][0],dp[-1][0]-nums[-1])
        else:
            return dp[-1][0]
