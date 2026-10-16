# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case (reached the last node)
            # return the node

        # Step Case
            # set a pointer to the recursed output
            # set the curr head's .next .next back to itself (because reverse)
            # set the curr head's.next to None
            # send the pointer out
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
