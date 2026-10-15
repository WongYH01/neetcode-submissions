# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case: Reached the end AKA root is null
        # recurse to the left
        # append value into array
        # recurse to the right
        res_list = []
        if not root:
            return []
        res_list += self.inorderTraversal(root.left)
        res_list += [root.val]
        res_list += self.inorderTraversal(root.right)
        return res_list
        
        