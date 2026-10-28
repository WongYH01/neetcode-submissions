# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        
        def checker(root, maxVal):
            if not root:
                return 0
            
            counter = 0

            if root.val >= maxVal:
                counter += 1
                maxVal = root.val
            
            counter += checker(root.left, maxVal)
            counter += checker(root.right, maxVal)

            return counter
        
        return checker(root, root.val)
