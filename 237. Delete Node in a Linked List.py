https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

# 1st attempt

#Runtime: 72 ms, faster than 10.18% of Python3 online submissions for Delete Node in a Linked List.
#Memory Usage: 14 MB, less than 95.40% of Python3 online submissions for Delete Node in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while (node.next.next):
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None

        
#2nd attempt  , onlu change the node needed
# Runtime: 52 ms, faster than 33.85% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.1 MB, less than 78.55% of Python3 online submissions for Delete Node in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
