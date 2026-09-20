# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set a slow and fast pointer
        # while the fast pointer is not null and the next is node is not null
            # advance slow by 1 node
            # advance fast by 2 nodes
            # check if both of them are at the same node
                # return true
        # return false
        slow_pointer, fast_pointer = head, head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False
        