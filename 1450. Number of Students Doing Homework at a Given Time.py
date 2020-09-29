#
#Runtime: 32 ms, faster than 91.27% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 14.1 MB, less than 5.38% of Python3 online submissions for Number of Students Doing Homework at a Given Time.

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        if queryTime > max(endTime): return 0
        
        counter = 0
        for i in range(len(endTime)):
            if queryTime <= endTime[i] and startTime[i] <= queryTime:
                counter += 1
        return counter
