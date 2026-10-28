# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # helper function taking root and maxVal int
        # Base Case: root is null
            # return 0

        # counter = 0

        # if curr node val >= maxVal
            # up counter
            # replace maxVal
        
        # counter += recurse .left
        # counter += recurse .right

        # return the counter

    def maxChecker(self, root, maxVal):
        if not root:
            return 0
        
        counter = 0
        if root.val >= maxVal:
            counter+=1
            maxVal = root.val
        
        counter += self.maxChecker(root.left,maxVal)
        counter += self.maxChecker(root.right,maxVal)

        return counter

    def goodNodes(self, root: TreeNode) -> int:
                
        return self.maxChecker(root, root.val)
