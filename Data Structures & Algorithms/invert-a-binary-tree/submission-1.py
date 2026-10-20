# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # manipulating .val method

        # Base Case: reached null node
            # return None
        
        # Step Case: 
            # set root.left to be recursed
            # set root.right to be recursed
            # set temp var as left val
            # set root.left.val to be 

        # return root

        if not root:
            return None
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        return root


