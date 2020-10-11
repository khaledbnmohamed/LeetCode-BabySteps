#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/



#Runtime: 544 ms, faster than 20.95% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
#Memory Usage: 19.3 MB, less than 97.88% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        if len(points) == 1: return 1
        dp = [0] * (len(points)+1)
        dp[0] = 0
        dp[1] = 1
        points.sort(key=lambda x: x[0])
        interval = [points[0][0],points[0][1]]
        for i in range(1,len(dp)-1):
            arrows,interval = self.isIntersected(points[i-1],points[i],interval)
            dp[i+1] = dp[i]+ arrows
        return dp[-1]
    def isIntersected(self,pointA,pointB,interval):
        if (pointB[0] <= interval[1] or pointB[0] <= interval[1]):
            interval=[max(interval[0],pointB[0]),min(interval[1],pointB[1])]
            return [0,interval]
        else:
            interval = pointB
            return [1,interval]
