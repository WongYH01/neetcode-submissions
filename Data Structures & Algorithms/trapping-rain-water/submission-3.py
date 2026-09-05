class Solution:
    def trap(self, height: List[int]) -> int:
        # L and R
        # set the max_left and max_right as the elem
        # while R > L
            # store L and R elems
            # check if L elem < R elem
                # calculate what you have now
                # add max(0, the eqn) to res_num
                # move L by 1
                # get the new max_left with max()
            # elif R elem > L elem
                # calculate what you have now
                # add max(0, the eqn) to res_num
                # move R back 1
                # get the new max_right with max()
        L, R = 0, len(height)-1
        res_num = 0
        max_left, max_right = height[L],height[R]
        while R > L:

            l_elem, r_elem = height[L],height[R]
            max_left = max(max_left,l_elem)
            max_right = max(max_right,r_elem)

            if l_elem <= r_elem:
                res_num += max(0, max_left-l_elem)
                L+=1
            elif r_elem < l_elem:
                res_num += max(0, max_right-r_elem)
                R-=1
        return res_num