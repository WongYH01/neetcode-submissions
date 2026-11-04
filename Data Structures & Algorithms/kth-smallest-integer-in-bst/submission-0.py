# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # value array

        # helper function to do in order traversal and append
            # Base Case: reach null node
                # return empty arr
            
            # concat recursed left
            # append curr value to arr
            # concat recursed right

            # return the arr
        
        # run the helper function
        # get the index-1 of the array

        val_arr = []

        def inOrder(root):
            if not root:
                return []
            
            res_arr = []

            res_arr += inOrder(root.left)
            res_arr.append(root.val)
            res_arr += inOrder(root.right)

            return res_arr
        
        val_arr = inOrder(root)
        return val_arr[k-1]


        
