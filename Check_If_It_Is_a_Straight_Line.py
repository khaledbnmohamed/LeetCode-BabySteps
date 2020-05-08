




#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        size = len(coordinates)
        if (size == 2):return True
        x1 = coordinates[0][0]
        x2 =coordinates[1][0]
        y1 = coordinates[0][1]
        y2 =coordinates[1][1]
        
        for i in range(1,size):
            if((x2-x1)*(coordinates[i][1]-y1) - (y2-y1)*(coordinates[i][0]-x1)) != 0 : return False
               
        return True
