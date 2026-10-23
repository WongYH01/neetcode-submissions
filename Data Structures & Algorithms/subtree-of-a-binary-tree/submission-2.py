# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), TypeGuard:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif (root1 and not root2) or (root2 and not root1):
            return False
        
        left_check = self.sameTree(root1.left, root2.left)
        right_check = self.sameTree(root1.right, root2.right)
        curr_check = root1.val == root2.val

        if left_check and right_check and curr_check:
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: check if both nodes are null
            # return True
            # elif either one of them
                # False

        # Step Case
            # check if the root val is the same as subRoot val
                # run the helper function
            # else
                # recurse root.left
                # recurse root.right

            # check if either is true
                # return true
            # return False
        
        if not root and not subRoot:
            return True
        elif (root and not subRoot) or (subRoot and not root):
            return False
        
        curr_check = False
        left_check = False
        right_check = False

        if root.val == subRoot.val:
            curr_check = self.sameTree(root, subRoot)

        if not curr_check:
            left_check = self.isSubtree(root.left, subRoot)
            right_check = self.isSubtree(root.right, subRoot)
        
        if curr_check or left_check or right_check:
            return True
        
        return False
            


