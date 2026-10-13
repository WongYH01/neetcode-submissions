# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Case: node is null, meaning reached end of tree
            # return the treenode of val

        # check if val is bigger than root val
            # recurse the right side of root
        # else
            # recurs the left side of root
        
        # return root
        
        if not root:
            return TreeNode(val=val)

        if val > root.val:
            root.right =  self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root
        