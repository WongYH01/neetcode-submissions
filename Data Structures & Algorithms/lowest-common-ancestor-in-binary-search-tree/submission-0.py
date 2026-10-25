# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base Case: reach null node
            # return null
        
        
        # the root where the split occurs is the LCA
        # if p and q more than curr val (both on right sub tree)
            # recurse right
        # elif p and q less than curr val (both on left sub tree)
            # recurse left
        # else (check if curr val is the same as p or q OR curr val causes the split)
            # return root
        
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        return root
