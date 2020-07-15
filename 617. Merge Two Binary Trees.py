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

        
#########################################
##2nd trial

# Runtime: 80 ms, faster than 67.27% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.7 MB, less than 57.65% of Python3 online submissions for Search in a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root:
            if root.val == val:
                return  root
            else:
                next_search = root.left if val < root.val else root.right
                return self.searchBST(next_search,val) 
        else:
            return None
