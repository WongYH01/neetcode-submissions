# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=, NoDefault0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # set curr node as first node
        # prev_node as nothing
        # while the curr node is not null
            # store the next node
            # point current node to the previous node 
            # set the curr node to the prev_node
            # set curr node to next node
        curr_node = head
        prev_node = None

        while (curr_node!=None):
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
        
        return prev_node
