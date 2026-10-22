# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Base Cases
        # If both are null nodes
            # True
        # If either one are null (meaning 1 reached a null node and 1 still at valid node AKA not match)
            # False
        
    # Step Case
        # left check recursing both left subtrees
        # right check recursing both right subtrees
        # check if curr node vals are the same

        # check if all 3 conditions are met
            # True
        # False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (q and not p):
            return False
        
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        curr_check = p.val == q.val

        if curr_check and left_check and right_check:
            return True
        return False