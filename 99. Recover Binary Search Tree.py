#https://leetcode.com/problems/recover-binary-search-tree/
#https://www.youtube.com/watch?v=bJBwOMPhe6Y



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.arr_rep = []
        def searchTree(root) -> None:
            if not root:
                return 
            else:
                searchTree(root.left)
                self.arr_rep.append(root)
                searchTree(root.right)
        
        searchTree(root)

        srted = sorted(i.val for i in self.arr_rep)
        
        for i in range(len(self.arr_rep)):
            self.arr_rep[i].val = srted[i]
        
