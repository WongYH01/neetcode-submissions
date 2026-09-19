# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # set a res dummy node
        # set pointer to res node
        # while either both .nexts are not empty
            # check if list 1 is empty
                # add list 2 nodes
                # move list 2 up
            # check if list 2 is empty
                # add list 1 nodes
                # move list 1 up
            # else (both not empty)
                # check if list1.val > list2.val
                    # set res pointer to list 2
                    # move list 2 up
                # else
                    # set res pointer to list 1
                    # move list 1 up
            # move res pointer up
        # return res.next
        
        res_node = ListNode()
        res_node_pointer = res_node

        while list1 or list2:
            if not list1:
                res_node_pointer.next = list2
                list2 = list2.next
            elif not list2:
                res_node_pointer.next = list1
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    res_node_pointer.next = list2
                    list2 = list2.next
                else:
                    res_node_pointer.next = list1
                    list1 = list1.next
            res_node_pointer = res_node_pointer.next
        
        return res_node.next
        


