#https://leetcode.com/problems/insert-into-a-binary-search-tree/


#Runtime: 128 ms, faster than 97.56% of Python3 online submissions for Insert into a Binary Search Tree.
#Memory Usage: 16.6 MB, less than 5.04% of Python3 online submissions for Insert into a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        self.traverseTree(root,val)
        return root
                    
    def traverseTree(self, root: TreeNode, val: int):
        if not root : return 
        else:
            if not(root.left) and (val < root.val ):
                root.left = TreeNode(val)
                return True
            elif not(root.right) and ( val > root.val ):
                root.right = TreeNode(val)
                return True
            else:
                next_search = root.left if val < root.val else root.right
                return self.traverseTree(next_search,val)

