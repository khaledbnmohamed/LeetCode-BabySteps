#https://leetcode.com/problems/time-needed-to-inform-all-employees/

#1st trial
#Runtime: 1892 ms, faster than 6.72% of Python3 online submissions for Time Needed to Inform All Employees.
#Memory Usage: 50.7 MB, less than 36.66% of Python3 online submissions for Time Needed to Inform All Employees.

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        if n ==1 : return 0
        if n == 2: return 1
        
        total_time = 0
        class TreeNode:
            def __init__(self, val=0):
                self.val = val
                self.children = []

            def add_child(self, obj):
                self.children.append(obj)
        self.nodes = []
        
        for i in range(n):
            self.nodes.append(TreeNode(i))
            
        root = self.nodes[headID]
        
        for i in range(len(manager)):
            if i != headID:
                self.nodes[manager[i]].add_child(self.nodes[i])
        

        def maxDepth(root) -> int:
            if not root: return 0
            
            maxdepth = 0
            for child in root.children:
                maxdepth =  max(maxDepth(child), maxdepth)     
        
            return maxdepth + informTime[root.val]
        
        return maxDepth(root)
