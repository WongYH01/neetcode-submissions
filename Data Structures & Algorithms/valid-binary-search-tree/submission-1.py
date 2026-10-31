# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function taking in root, lowest and highest value
            # Base Case: root is null
                # True
            
            # curr check if the root.val is between lowest and hightest
            # left check recursing setting the highest as min(curr highest, root.val) 
                # [Because moving left caps the highest the val can go]
            # right check recursing setting the lowest as max(curr lowest, root.val)
                # [Because moving right caps the lowest the val can go]
            
            # check if all conditions meet
                # return True
            # return False

        def helper(root, highest, lowest):
            if not root:
                return True

            curr_check = highest > root.val > lowest
            left_check = helper(root.left,min(highest, root.val), lowest)
            right_check = helper(root.right,highest, max(lowest, root.val))

            if curr_check and left_check and right_check:
                return True
            return False
        return helper(root, math.inf, -math.inf)
