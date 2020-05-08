# https://leetcode.com/problems/range-sum-of-bst/
# Steps :
# 1) Using stack


############################################
# trial # 1
# NOT WORKING approach
############################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        
        range
        sum1 = self.searchLeftNode(root.left, L,sum)
        sum2 = self.searchRightNode(root.right, R,sum)
        print("sum2",sum2)
        print("sum1",sum1)
        result = 0
        if sum2 is not None and sum2 is not None:
            result = sum1 + sum2
        elif sum2 is None:
            result = sum1 
        elif sum1 is None:
            result = sum2
        return result + root.val
        
    def searchLeftNode(self, root, child_node,sum):
        if  root :
            
            if root.val == child_node:
                return sum+child_node  
            if root.left and root.left.val== child_node:
                return sum+child_node+root.val
            if root.right and root.right.val== child_node:
                return sum+child_node+root.val
            elif root:
                if root.val < child_node:
                    return self.searchLeftNode(root.right, child_node,sum) 
                else:
                    sum += root.val
                    return self.searchLeftNode(root.left, child_node,sum)

    def searchRightNode(self, root, child_node,sum):
        if  root :
            if root.val == child_node:
                return sum+child_node  
            if root.left and root.left.val== child_node:
                return sum+child_node+root.val
            if root.right and root.right.val== child_node:
                return sum+child_node+root.val
            elif root:
                if root.val < child_node:
                    return self.searchRightNode(root.right, child_node,sum) 
                else:
                    sum += root.val
                    return self.searchRightNode(root.left, child_node,sum)
