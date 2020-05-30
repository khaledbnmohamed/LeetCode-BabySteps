# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Runtime: 44 ms, faster than 53.94% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.6 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.

#  #1 trial 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (not head ) : return head
        head1 = head
        while head.next:
            value = head.val
            while head.next and head.next.val == value:
                head.next= head.next.next

            if head.next:
                head = head.next
        return head1
####################################################
# #2 trial 

# Runtime: 44 ms, faster than 53.94% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.
    
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head1 = head
        try:
            while head.next:
                value = head.val
                while head.next.val == value:
                    head.next= head.next.next

                if head.next:
                    head = head.next
        except:
            return head1
        return head1        
