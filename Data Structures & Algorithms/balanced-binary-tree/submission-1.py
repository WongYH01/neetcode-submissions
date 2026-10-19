# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        # Base Case: When hit null
            # return 0
        
        # Step Case: 
            # recurse root.left
            # recurse root.right
            # return 1 + max(root.left, root.height)
        
        if not root:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return 1 + max(left_height, right_height)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Base Case: reached a null node
            # return True

        # Step Case

        if not root:
            return True
        
        left_check = self.isBalanced(root.left)
        root_left_height = self.getHeight(root.left)

        right_check = self.isBalanced(root.right)        
        root_right_height = self.getHeight(root.right)

        if abs(root_left_height-root_right_height)>1:
            return False
        
        if left_check and right_check:
            return True
        else:
            return False
        


