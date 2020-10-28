

https://leetcode.com/problems/linked-list-cycle-ii/submissions/

#Runtime: 44 ms, faster than 94.42% of Python3 online submissions for Linked List Cycle II.
#Memory Usage: 16.9 MB, less than 99.98% of Python3 online submissions for Linked List Cycle II.
#https://www.youtube.com/watch?v=zbozWoMgKW0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return None

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if (slow == fast):
                return self.find_start_loop(head,slow)
                
    def find_start_loop(self, head, matching_node):
        while head != matching_node:
            head = head.next
            matching_node = matching_node.next
            
        return head
        
        
