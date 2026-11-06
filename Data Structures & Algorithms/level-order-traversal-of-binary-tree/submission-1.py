# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue
        # res arr

        # check if root valid
            # place into queue
        
        # while the queue not empty
            # tmp array
            # iterate thru the queue 
                # popleft
                # check if have .left
                    # add
                # check if have .right
                    # add
        
        queue = deque()
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
            res_arr.append(tmp_arr)
        return res_arr
            




