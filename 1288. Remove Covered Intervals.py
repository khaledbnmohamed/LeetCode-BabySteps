https://leetcode.com/problems/remove-covered-intervals/submissions/

#Runtime: 5128 ms, faster than 5.08% of Python3 online submissions for Remove Covered Intervals.
#Memory Usage: 14.6 MB, less than 5.08% of Python3 online submissions for Remove Covered Intervals.


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        toBeRemoved = {}
        for interval in intervals:
            for j in range(len(intervals)):
                if intervals[j] != interval:
                    if interval[0] >= intervals[j][0] and interval[1] <= intervals[j][1]:
                        toBeRemoved[str(interval[0])+str(interval[1])]= 0
                    elif interval[0] <= intervals[j][0] and interval[1] >= intervals[j][1]:
                        toBeRemoved[str(intervals[j][0]) + str(intervals[j][1])]=0

        return len(intervals)-len(toBeRemoved)
            
