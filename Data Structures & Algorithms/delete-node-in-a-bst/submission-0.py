# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper function to find the min node taking root as param
        # while curr node and node.left
            # set to node left
        # return the node val
    def findMinNode(self, root):
        curr_node = root
        while curr_node and curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: check if curr tree node is none
            # return None

        # check if val is bigger than node's val
            # move right
        # check if val is smaller than node's val
            # move left
        # else (found val)
            # if dont have left of node
                # return the right of node
            # elif dont have right of node
                # return left of node
            # else (Got both left and right node)
                # find the min node from the right side cause if left side then will mess up order
                # set the curr node value to the min node value
                # update the right side by deleting the min value
        # return the root

        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.findMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right,min_node.val)
        return root




