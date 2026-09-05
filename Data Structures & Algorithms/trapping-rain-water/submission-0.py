class Solution:
    def trap(self, height: List[int]) -> int:
        # empty array of arrays with 2 elems, left max and right max
        # left max = 0
        # iterate height left to right
            # set the [empty][i][0] to be left max
            # get the max

        # right max
        # iterate height right to left

        # res_counter
        # iterate through height with k
            # get the index of reference_array
            # find min and - the current elem

        reference_max_array = [[0,0] for _ in range(len(height))]

        left_max = 0
        for i in range(len(height)):
            reference_max_array[i][0] = left_max
            left_max = max(left_max, height[i])
        
        right_max = 0
        for j in range(len(height)-1, -1, -1):
            reference_max_array[j][1] = right_max
            right_max = max(right_max, height[j])

        res_num = 0
        for k in range(len(height)):
            boundaries = reference_max_array[k]
            res_num += max(min(boundaries)-height[k],0)
        
        return res_num

        