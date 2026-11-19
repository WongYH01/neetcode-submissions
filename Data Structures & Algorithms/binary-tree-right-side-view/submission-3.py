# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # queue
        # res array

        # check if root exists
            # push root into queue

        # while queue is not empty
            # iterate thru queue with i
                # popleft the queue

                # check whether the popped got left
                    # add to queue
                # check whether the popped got right
                    # add to queue
        
        queue = deque()
        res_array = []

        if root:
            queue.append(root)

        while queue:
            res_array.append(queue[-1].val)
            for i in range(len(queue)):
                curr_root = queue.popleft()

                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)

        return res_array
        