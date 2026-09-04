class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # var to store max area
        # L and R
        # while L < R
            # min(L,R) * (R-L)
            # if L is smaller
                # L+=1
            # if R is bigger
                # R-=1
        
        maxer_area = 0
        L, R = 0, len(heights)-1
        while L < R:
            L_height = heights[L]
            R_height = heights[R]
            height = min(L_height,R_height)
            area = height * (R-L)

            maxer_area = max(area, maxer_area)

            if L_height < R_height or L_height == R_height:
                L+=1
            else:
                R-=1
        return maxer_area

        