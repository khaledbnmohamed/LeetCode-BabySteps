#https://leetcode.com/problems/search-in-a-binary-search-tree/
#Runtime: 108 ms, faster than 17.65% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.6 MB, less than 88.11% of Python3 online submissions for Search in a Binary Search Tree.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return  root
            else:
                node = self.searchBST(root.left,val) 
                return node if node else self.searchBST(root.right,val) 
        else:
            return None
