# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # set a var to carry on

        # while either pointers are still valid
            # check if 

            # (condition where both l pointers are valid)
                # get the values of both pointers
                # add them together

                # check if more than 9
                    # 
            
            # move both pointers to their next

        carry_on = 0
        res = ListNode()
        res_pointer = res
        l1_pt, l2_pt = l1, l2
        

        while carry_on or l1_pt or l2_pt:
            l1_val, l2_val = 0,0
            if l1_pt:
                l1_val = l1_pt.val
            if l2_pt:
                l2_val = l2_pt.val

            l_sums = l1_val+l2_val+carry_on

            carry_on = l_sums//10
            res_node_val = l_sums-(carry_on*10)
            res_node = ListNode(res_node_val)

            res_pointer.next = res_node

            res_pointer = res_pointer.next

            if l1_pt:
                l1_pt = l1_pt.next
            if l2_pt:
                l2_pt = l2_pt.next
        
        return res.next

        