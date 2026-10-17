# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinRoot(self, root: TreeNode):
        while root and root.left:
            root = root.left
        return root


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: When key does not exist AKA now at 


        # Step Case
        # check if key bigger than node val

        # elif key smaller than node val

        # else: found key
            # check if got left sub tree

            # check if got right sub tree

            # else: got both subtrees
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_node = self.findMinRoot(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root


        