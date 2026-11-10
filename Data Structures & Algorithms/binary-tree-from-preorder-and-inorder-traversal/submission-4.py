# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        preorder_idx = 0

        def helper(low, high):
            nonlocal preorder_idx
            nonlocal inorder_map

            if low == high:
                return None
            
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)
            split_idx = inorder_map[root_val]

            root.left = helper(low,split_idx)
            root.right = helper(split_idx + 1,high)

            return root


        return helper(0,len(preorder))

        