# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow and fast pointer but fast is 1 node in front
            # get the mid point AKA start of 2nd half

        # declare 2nd reverse pointer as None
        # iterate the normal 2nd half
            # store normally next node
            # set the next node to 2nd reverse pointer
            # set the normal 2nd half pointer to normal next node
        
        s,f = head, head.next
        while f and f.next:
            s,f = s.next,f.next.next

        second = s.next
        s.next = None

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        first = head

        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2

        # while second:
        #     print(second.val, end=" -> ")
        #     second = second.next

