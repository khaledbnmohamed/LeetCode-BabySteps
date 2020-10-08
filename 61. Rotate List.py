#https://leetcode.com/problems/rotate-list/

#Runtime: 48 ms, faster than 23.11% of Python3 online submissions for Rotate List.
#Memory Usage: 14 MB, less than 29.39% of Python3 online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next is None: return head
        start = head
        nodeCount = 1
        while head.next is not None:
            head = head.next
            nodeCount += 1
        head = start
        k = k%nodeCount
        while k>0:
            start = head
            while head.next.next is not None:
                head = head.next
            myNext = head.next
            head.next = None
            myNext.next = start
            head = myNext
            k-= 1
        return head
