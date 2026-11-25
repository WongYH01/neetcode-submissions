class Node:
    def __init__(self,key,val):
        self.key,self.val = key, val
        self.next, self.prev = None, None
        

class LRUCache:

    def __init__(self, capacity: int):
        # set capacity
        # set hashmap: key is key, val is node class

        # 2 helper node, least freq and most freq, link both tgt

        self.capacity = capacity
        self.key_map = {}

        self.least_freq = Node(None, None)
        self.most_freq = Node(None, None)
        self.least_freq.next = self.most_freq
        self.most_freq.prev = self.least_freq
        

    def get(self, key: int) -> int:
        # check if the key exists in hashmap
            # get the node with val
            # use remove helper function 
            # use add helper function

            # return the val
        # return -1
        if key in self.key_map:
            node = self.key_map[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        return -1

    # helper function add_node taking val and key
        # create a new node class 

        # take the node before most_freq
        # set .next of prev node to be new node
        # set .next of new node to most_freq

        # set .prev of most_freq to be new node
        # set .prev of new node to prev node
    def add_node(self, new_node):
        prev_node = self.most_freq.prev

        prev_node.next = new_node
        new_node.next = self.most_freq

        self.most_freq.prev = new_node
        new_node.prev = prev_node
    
    # helper function remove_node taking the node
        # get the next node
        # get the prev node

        # set next of prev node to next node
        # set prev of next node to prev node
        # set next and prev of selected node to none
    def remove_node(self,selected_node):
        next_node = selected_node.next
        prev_node = selected_node.prev

        prev_node.next = next_node
        next_node.prev = prev_node
        selected_node.prev,selected_node.next = None, None
        
    
    def put(self, key: int, value: int) -> None:
        # check if key exists in key_map
            # get the node from map
            # use the remove_node helper

        # new node with key and val
        # use the add_node helper with new node as param
        # insert the node as value to map key

        # check if the length of map exceeds cap
            # get the node right after least_freq
            # get the key
            # remove from hashmap with key
            # use remove helper
        if key in self.key_map:
            node_to_remove = self.key_map[key]
            self.remove_node(node_to_remove)
        
        new_node = Node(key,value)
        self.add_node(new_node)
        self.key_map[key] = new_node

        if len(self.key_map) > self.capacity:
            selected_node = self.least_freq.next
            selected_key = selected_node.key
            self.key_map.pop(selected_key)
            self.remove_node(selected_node)

        
