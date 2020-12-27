#https://leetcode.com/problems/swap-nodes-in-pairs/


#2nd attempt

# Runtime: 24 ms, faster than 94.96% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 89.83% of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        if head.next == None: return head
        self.nodes = []
        while head.next and head.next.next:
            self.nodes.append(head.next)
            self.nodes.append(head)
            head = head.next.next

        if head.next:
            self.nodes.append(head.next)
        
        self.nodes.append(head)

        for i in range(0,len(self.nodes)-1):
            self.nodes[i].next = self.nodes[i+1]
            

        self.nodes[-1].next = None
            
            
        return  self.nodes[0]







#Runtime: 32 ms, faster than 55.62% of Python3 online submissions for Swap Nodes in Pairs.
#Memory Usage: 14.2 MB, less than 68.89% of Python3 online submissions for Swap Nodes in Pairs.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        if head.next == None: return head
        self.nodes = []
        while head:
            self.nodes.append(head)
            head = head.next
            
        start = self.nodes[1]
        for i in range(0,len(self.nodes)-1,2):
            temp = self.nodes[i] 
            self.nodes[i]= self.nodes[i+1]
            self.nodes[i+1] = temp
            self.nodes[i].next = self.nodes[i+1]

        for i in range(len(self.nodes)-1):
            self.nodes[i].next = self.nodes[i+1]
            

            
        self.nodes[-1].next = None
            
            
        return start
