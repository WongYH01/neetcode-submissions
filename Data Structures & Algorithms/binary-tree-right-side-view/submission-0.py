# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # new queue
        # levels array
        # res array

        # check if root is valid
            # add to queue

        # while queue has length
            # tmp array
            # iterate thru queue with index
                # pop from queue
                # add to levels array

                # check if have a .left
                    # add to queue
                # check if have a .right
                    # add to queue
        
        # iterate thru levels array
            # append the last element of each array
        
        # return res array

        queue = deque()
        level_arr = []

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
                
            level_arr.append(tmp_arr)
        
        res_arr = []
        for curr_level in level_arr:
            res_arr.append(curr_level[-1])

        return res_arr

        