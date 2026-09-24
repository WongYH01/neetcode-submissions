# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # set a var for carry on
        # res node
        # pointer to res node
        # have l1 and l2 pointers

        # while carry_on or l1 or l2 are valid
            # set inital l1 and l2 vals to 0
            # check if l1 is valid
                # set the val on that
            # check if l2 is valid
                # set the val on that
            
            # get the sum of l1 l2 and carry_on
            # update carry_on to be //10 of sum
            # get the curr node val to be sum - carry_on*10
            # create new node with new value
            # point res pointer next to new node
            # move res pointer to new node

            # check if l1 is not None
                # move l1 pointer to the next node
            # check if l2 is not None
                # move l2 pointer to the next node
        
        # return the res.next

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

        