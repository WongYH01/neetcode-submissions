class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pair_stack = []
        max_area = 0

        for i in range(len(heights)):
            start = i

            while pair_stack and pair_stack[-1][1] > heights[i]:
                pop_start, pop_height = pair_stack.pop()
                max_area = max(max_area, pop_height * (i-pop_start))
                start = pop_start
            
            pair_stack.append((start, heights[i]))
        
        while pair_stack:
            remain_start, remain_height = pair_stack.pop()
            max_area = max(max_area, remain_height*(len(heights)-remain_start))

        return max_area
        