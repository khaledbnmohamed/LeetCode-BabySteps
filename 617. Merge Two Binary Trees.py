#https://leetcode.com/problems/merge-two-binary-trees/

#Runtime: 156 ms, faster than 9.60% of Python3 online submissions for Merge Two Binary Trees.
#Memory Usage: 14.8 MB, less than 81.98% of Python3 online submissions for Merge Two Binary Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1
        else:
            return t2 or t1

        
