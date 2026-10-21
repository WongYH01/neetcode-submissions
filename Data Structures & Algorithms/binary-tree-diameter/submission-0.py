# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLength(self, root):
        if not root:
            return 0
        
        length_left = self.getLength(root.left)
        length_right = self.getLength(root.right)

        return 1 + max(length_left, length_right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base Case
            # root is null
            # return 0
        
        # Step Case
            # get length of root.left
            # get length of root.right
            # sum up
        if not root:
            return 0
                
        left_length = self.getLength(root.left)
        right_length = self.getLength(root.right)
        
        best_root = left_length + right_length
        best_left = self.diameterOfBinaryTree(root.left)
        best_right = self.diameterOfBinaryTree(root.right)

        return max(best_root, best_left, best_right)




