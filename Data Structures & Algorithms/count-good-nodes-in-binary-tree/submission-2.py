# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # helper function as max val param
            # Base Case: reached a null root
                # return 0
            
            # counter = 0
            # check if the curr node >= max val
                # add counter by 1
                # replace max val
            
            # recurse left and add to counter
            # recurse right and add to counter
            # return counter
        
        def helper(root, max_val):
            if not root:
                return 0
            
            counter = 0
            
            if root.val >= max_val:
                counter += 1
                max_val = root.val
            
            counter += helper(root.left,max_val)
            counter += helper(root.right,max_val)

            return counter
        
        return helper(root,root.val)