# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack
        # rank_counter = 0

        # while still have have value
            # append the curr root to stack
            # change curr root to point to .left
        
        # while the stack not empty
            # pop out the visiting node
            
            # up counter by 1
            # if the counter == k
                # return the val
            
            # check if have .right
                # pointer
                # while pointer exists
                    # append node to stack
                    # move pointer to the .left
        stacker = []
        rank_counter = 0
        tmp_1 = root

        while tmp_1:
            stacker.append(tmp_1)
            tmp_1 = tmp_1.left
        
        while stacker:
            node_vis = stacker.pop()

            rank_counter+=1
            if rank_counter == k:
                return node_vis.val
            
            if node_vis.right:
                tmp_2 = node_vis.right
                while tmp_2:
                    stacker.append(tmp_2)
                    tmp_2 = tmp_2.left
        
        return 0





