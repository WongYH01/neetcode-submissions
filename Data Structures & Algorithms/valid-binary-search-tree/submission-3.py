# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper func with min, max and root as params
            # Base Case: reach a null node
                # return true
            
            # curr check if the curr root is in between min and max
            # left check recursing function setting the max threshold 
            # right check recursing function setting the min threshold 

            # return AND of all 3
        
        def helper(root, min_cap, max_cap):
            if not root:
                return True
            
            curr_check = max_cap > root.val > min_cap
            left_check = helper(root.left, min_cap, min(root.val,max_cap))
            right_check = helper(root.right, max(root.val, min_cap), max_cap)

            return (curr_check and left_check and right_check)

        return helper(root, -math.inf, math.inf)