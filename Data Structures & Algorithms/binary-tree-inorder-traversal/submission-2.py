# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case: Reaches null node
            # return empty array
        
        # result arr

        # Step Case:
            # concat recursed root.left to res arr
            # append res arr the root val itself
            # concat recursed root.right to res arr


        if not root:
            return []
        
        res_array = []

        res_array += self.inorderTraversal(root.left)
        res_array.append(root.val)
        res_array += self.inorderTraversal(root.right)

        return res_array
