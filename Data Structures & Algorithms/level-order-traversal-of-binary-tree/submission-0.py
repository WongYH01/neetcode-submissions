# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # empty res array
        # empty queue

        # check if root exists
            # add root to queue
        
        # while the queue is not empty
            # tmp arr
            # iterate thru the queue
                # pop the root from queue
                # append .val into tmp

                # check if .left exists
                    # add to queue
                # check if .right exists
                    # add to queue

        res_arr = []
        res_queue = deque()

        if root:
            res_queue.append(root)

        while res_queue:
            tmp_arr = []
            for i in range(len(res_queue)):
                curr_root = res_queue.popleft()
                tmp_arr.append(curr_root.val)

                if curr_root.left:
                    res_queue.append(curr_root.left)

                if curr_root.right:
                    res_queue.append(curr_root.right)
            res_arr.append(tmp_arr)
        
        return res_arr