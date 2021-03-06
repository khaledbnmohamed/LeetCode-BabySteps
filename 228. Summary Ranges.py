#https://leetcode.com/problems/summary-ranges/
# 2nd attempt

# Runtime: 28 ms, faster than 71.99% of Python3 online submissions for Summary Ranges.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Summary Ranges.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        stack = [nums[0]]
        final_array = []  
        start = nums[0]
        
        for i in range(1,len(nums)):
            start += 1
            if start != nums[i]:
                start_element = stack.pop()
                
                self.appender(final_array,start_element, nums[i-1])
                start = nums[i]
                stack.append(start)
                
            elif not stack:
                stack.append(nums[i])
                
        self.appender(final_array,stack.pop() if stack else nums[len(nums)-1], nums[len(nums)-1]) 
        
        return final_array
    
    def appender(self, final_array, start, end):
            if start == end:
                final_array.append( f"{start}")
            else:
                final_array.append(f"{start}->{end}")
                
#Runtime: 28 ms, faster than 71.99% of Python3 online submissions for Summary Ranges.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Summary Ranges.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        stack = []
        final_array = []
        
        start = nums[0]
        stack.append(start)
        for i in range(1,len(nums)):
            start += 1
            if start != nums[i]:
                start_element = stack.pop()
                
                if start_element == nums[i-1]:
                    final_array.append( f"{start_element}")
                    
                else:
                    final_array.append(f"{start_element}->{nums[i-1]}")
                    
                start = nums[i]
                stack.append(start)
                
            elif not stack:
                stack.append(nums[i])
                
        if stack:
            start_element = stack.pop()

            if start_element == nums[len(nums)-1]:
                final_array.append( f"{start_element}")

            else:
                final_array.append(f"{start_element}->{nums[len(nums)-1]}")
        else:
            final_array.append(f"{nums[len(nums)-1]}")

        return final_array
