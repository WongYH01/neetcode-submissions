# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        level_arr = []
        res_arr = []

        if root:
            queue.append(root)
        
        while queue:
            tmp_arr = []
            for i in range(len(queue)):
                popped = queue.popleft()
                tmp_arr.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                
                if popped.right:
                    queue.append(popped.right)
                
            res_arr.append(tmp_arr[-1])

        return res_arr