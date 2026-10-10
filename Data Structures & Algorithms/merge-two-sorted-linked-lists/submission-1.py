# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_node = ListNode()
        res_node_ptr = res_node
        while list1 or list2:
            if not list1:
                res_node_ptr.next = list2
                list2 = list2.next
            elif not list2:
                res_node_ptr.next = list1
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    res_node_ptr.next = list1
                    list1 = list1.next
                else:
                    res_node_ptr.next = list2
                    list2 = list2.next
            res_node_ptr = res_node_ptr.next

        return res_node.next