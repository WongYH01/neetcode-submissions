# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # declare a dummy node to handle edge case where the node to remove is the start
        # set fast and slow to be the head and dummy

        # counter
        # while the counter is 1 below n
            # move fast by 1
            # up the counter
        
        # while the next node of fast is not null
            # move fast and slow by 1
        # (Will now be just before the node to remove)
        # set the next node of slow to be .next.next

        # return dummy.next to get the start

        dummy = ListNode(0,head)
        fast, slow = head,dummy
        counter = 0

        while counter < n-1:
            fast = fast.next
            counter+=1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next




    