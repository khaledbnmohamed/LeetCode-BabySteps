#https://leetcode.com/problems/swap-nodes-in-pairs/

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
