#https://leetcode.com/problems/rotate-list/

#2nd trial

# Runtime: 28 ms, faster than 98.24% of Python3 online submissions for Rotate List.
# Memory Usage: 14.2 MB, less than 5.19% of Python3 online submissions for Rotate List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # if no rotations return
        if not k: return head
        if not head or head.next is None: return head
        
        start = head
        nodeCount = 1
        # start counting node numbers to know how many compelte cycles within K
        while start.next is not None:
            start = start.next
            nodeCount += 1
        
        # know the real non duplicated rotations
        k = k%nodeCount
        
        # if no rotations return
        if not k: return head

        steps = nodeCount-k
        start = head
        
        if(steps == 1): myNext = head.next
            
        # reach the node where all nodes after are rotated
        while steps > 1:
            head = head.next
            steps -= 1
            
        myNext = head.next
        newStart = myNext
        
        while myNext.next is not None:
            myNext = myNext.next
        
        #slice the linked list all together
        head.next = None
        myNext.next = start
        return newStart




################################
#1st trial
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
####################################################
