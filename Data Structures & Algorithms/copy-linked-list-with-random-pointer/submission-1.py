"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a pointer to head
        # hashmap
        # while that is not null
            # create a new node with the value
            # set key as old and value as new node
            # go next old node

        # another pointer to head
        # iterate pointer
            # grab the .next node
            # grab the .random node
            # set a pointer to new node w/ hashmap
            # the new node .next is the value in hashmap
            # the new node .random is the value in hashmap
            # go next old node

        # set a pointer to the hashmap value with key
        # return said pointer

        if not head:
            return None

        setup = head
        node_map = {}
        while setup:
            new_node = Node(setup.val)
            node_map[setup] = new_node
            setup = setup.next
        
        mapping = head
        while mapping:
            old_next = mapping.next
            old_random = mapping.random

            curr_new_node = node_map[mapping]

            if old_next not in node_map:
                curr_new_node.next = None
            else:
                curr_new_node.next = node_map[old_next]

            if old_random not in node_map:
                curr_new_node.random = None
            else:
                curr_new_node.random = node_map[old_random]

            mapping = mapping.next
        
        res_list = node_map[head]

        return res_list

