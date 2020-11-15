#https://leetcode.com/problems/poor-pigs/



#Runtime: 28 ms, faster than 71.83% of Python3 online submissions for Poor Pigs.
#Memory Usage: 14.3 MB, less than 21.13% of Python3 online submissions for Poor Pigs.

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        number_of_tests = int(minutesToTest/minutesToDie)
        number_of_pigs = math.log10(buckets) / math.log10(number_of_tests+1)
        return math.ceil(number_of_pigs)
