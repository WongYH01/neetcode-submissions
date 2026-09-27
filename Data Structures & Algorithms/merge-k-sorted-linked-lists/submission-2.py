# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # helper function to merge 2 sorted lists of nodes
    def merge_two_lists(self, l1, l2):
        # have a res node
        # pointer to res node

        # while l1 or l2 still exist
            # check if l1 finish alrdy
                # point res node to l2
                # move l2 up
            # check if l2 finish alrdy
                # point res node to l1
                # move l1 up
            # else
                # check if l1 is < l2
                    # point res to l1
                    # move l1 up
                # else
                    # point res to l2
                    # move l2 up
        
        # return res node.next
        res_node = ListNode()
        res = res_node

        while l1 or l2:
            
            if not l1:
                res.next = l2
                l2 = l2.next

            elif not l2:
                res.next = l1
                l1 = l1.next

            else:
                if l1.val < l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
            
            res = res.next

        return res_node.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # check if the list does not exist
            # return none
        
        # while the length of lists is more than 1
            # empty list
            # iterate lists with i with step of 2
                # define curr list
                # check if i+1 is <= len-1
                    # set next list to next list
                # set next list to none
                # use helper function on both lists
                # append to empty list
            # set lists to be the new list
        if not lists:
            return None
        
        while len(lists) > 1:
            lister= []
            for i in range(0,len(lists),2):
                list_1 = lists[i]

                if (i+1) < len(lists):
                    list_2 = lists[i+1]
                else:
                    list_2 = None

                merged_list = self.merge_two_lists(list_1, list_2)
                lister.append(merged_list)
            lists = lister
        
        return lists[0]
