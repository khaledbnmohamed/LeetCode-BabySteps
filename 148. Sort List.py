# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        if head.next == None: return head
        
        newHead= head
        arr= []
        while head.next:
            cycleHead = head.next.next
            print("head",head.val)
            # if(cycleHead): print(" befre cycleHead",cycleHead.val)

            while cycleHead.next:
                # print("cycleHead",cycleHead.val)

                if head.next.val > cycleHead.val:
                    # if(cycleHead.next): print(" cycleHead.next", cycleHead.next.val)
                    temp = head.next
                    head.next = cycleHead
                    print(" head.next", cycleHead.val)

                    temp.next = cycleHead.next
                    cycleHead.next = temp
                cycleHead = cycleHead.next
            head = head.next
        return newHead          
        # arr.sort()
        # newHead.val=arr[0]
        # head = newHead
#         for i in range(1,len(arr)):
#             newHead.next.val = arr[i]
#             newHead = newHead.next
            
        # return head
