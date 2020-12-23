#https://leetcode.com/problems/maximum-depth-of-binary-tree/


#Runtime: 40 ms, faster than 72.49% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 16 MB, less than 47.58% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
