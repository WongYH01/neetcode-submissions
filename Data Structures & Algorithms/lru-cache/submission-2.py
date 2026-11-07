class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val = key, val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        # dummy sentinels: left side = least recent, right side = most recent
        self.least_freq_node, self.most_freq_node = Node(0, 0), Node(0, 0)
        self.least_freq_node.next = self.most_freq_node
        self.most_freq_node.prev = self.least_freq_node

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove_node(node)   # detach from the current position
            self.add_node(node)      # re-attach at the most recent end
            return node.val          # return the value, not the node
        return -1

    def add_node(self, node_to_add):
        prev_freq_node = self.most_freq_node.prev

        node_to_add.prev = prev_freq_node
        node_to_add.next = self.most_freq_node

        prev_freq_node.next = node_to_add
        self.most_freq_node.prev = node_to_add

    def remove_node(self, node_to_remove):
        prev_node = node_to_remove.prev
        next_node = node_to_remove.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            # key exists: unlink the old node (a Node, not .val)
            self.remove_node(self.node_map[key])
        elif len(self.node_map) >= self.capacity:
            # cache full: evict the least recent node (right after the left sentinel)
            least_node = self.least_freq_node.next
            self.remove_node(least_node)
            self.node_map.pop(least_node.key)

        # insert a fresh node at the most recent end and map the key to it
        new_node = Node(key, value)
        self.node_map[key] = new_node
        self.add_node(new_node)