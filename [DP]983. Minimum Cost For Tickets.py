#Runtime: 68 ms, faster than 27.52% of Python3 online submissions for Minimum Cost For Tickets.
#Memory Usage: 13.8 MB, less than 81.16% of Python3 online submissions for Minimum Cost For Tickets.



class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] +1)
        dp[0] = 0
        total_day = days[-1]
        days = set(days)
        for day in range(1,total_day+1):
            if day in days:
                dp[day]= min(dp[day-1]+costs[0],dp[max(day-7,0)]+costs[1], dp[max(day-30,0)]+costs[2])
            else:
                dp[day]=dp[day-1]

        return dp[-1]
                
                
            
