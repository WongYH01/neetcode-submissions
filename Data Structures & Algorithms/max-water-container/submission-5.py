class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set L and R to be start and end

        # while L < R
            # get the max width by maxing the elems
            # get the length

            # get the area
            # max the area and curr max area

            # if L > R
                # move R down by 1
            # move L up by 1
        # return max area

        L,R = 0, len(heights)-1
        max_area = 0

        while L < R:
            # print(f"L:{L}")
            # print(f"R:{R}")

            max_width = min(heights[L],heights[R])
            length = R-L

            area = max_width*length
            max_area = max(area, max_area)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        
        return max_area