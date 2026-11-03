# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), TypeGuard:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function taking in root, min and max value
            # check if the current root is bigger than the min and smaller than the right
            # left check recurses function but now setting the highest it can go
            # right check recurses function but now setting the lowest it can go
        
        def helper(root, highest, lowest) -> bool:
            if not root:
                return True

            curr_check = root.val > lowest and root.val < highest
            left_check = helper(root.left, min(highest, root.val), lowest)
            right_check = helper(root.right, highest, max(lowest, root.val))

            if curr_check and left_check and right_check:
                return True
            return False
        
        return helper(root,math.inf,-math.inf)
        