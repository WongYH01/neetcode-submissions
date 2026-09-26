# Declare a doubly linked node class

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        # initalize cap
        # have hashmap
        # have dummy nodes for most and least used
        # connect dummy nodes together

        self.capacity = capacity
        self.node_map = {}

        self.least_recent, self.most_recent =  Node(0,0), Node(0,0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent       

    # helper function to remove from linked list
        # get the prev node of the node to remove
        # get the next node of the node to remove
        # set the prev node.next to be the next node instead
        # set the next node.prev to be the prev node instead
    def remove_node(self, node_to_remove):
        prev_node = node_to_remove.prev
        next_node = node_to_remove.next

        prev_node.next = next_node
        next_node.prev = prev_node
    

    # helper function to add node to linked list
        # get the previous node
        # set the new node.prev to the previous node
        # set the new node.next to the most used node

        # set the previous node.next to the new node
        # set the most recent node.prev as the new node
    def add_node(self, node_to_add):
        prev_node = self.most_recent.prev
        
        node_to_add.prev = prev_node
        node_to_add.next = self.most_recent

        prev_node.next = node_to_add
        self.most_recent.prev = node_to_add
    

    def get(self, key: int) -> int:
        # check if key exist in hashmap
            # use helper function to remove and then add node
            # return the node value
        # else
            # return -1
        
        if key in self.node_map:
            self.remove_node(self.node_map[key])
            self.add_node(self.node_map[key])
            return self.node_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # check if the key exists in the hashmap
            # update the value of the node
            # remove the node
        # elif the length of the hashmap >= capacity
            # get the node right after the least used node
            # remove the least used node
            # remove the least used key in hashmap
        # create a new node 
        # add the node to the latest

        if key in self.node_map:
            key_node = self.node_map[key]
            key_node.val = value
            self.remove_node(key_node)
        elif len(self.node_map) >= self.capacity:
            least_recent_node = self.least_recent.next
            self.remove_node(least_recent_node)
            self.node_map.pop(least_recent_node.key)
        
        new_node = Node(key,value)
        self.node_map[key] = new_node
        self.add_node(new_node)

        pass
