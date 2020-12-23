#https://leetcode.com/problems/balanced-binary-tree/

#Runtime: 56 ms, faster than 44.47% of Python3 online submissions for Balanced Binary Tree.
#Memory Usage: 19.1 MB, less than 20.22% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        self.Bal = True

        def searchTree(root)-> int:
            if root is None: 
                return 0
            lt,rt = searchTree(root.left), searchTree(root.right)
            if abs(lt - rt) > 1: self.Bal = False
            return max(lt,rt) + 1
                
        
        searchTree(root)

        return self.Bal
