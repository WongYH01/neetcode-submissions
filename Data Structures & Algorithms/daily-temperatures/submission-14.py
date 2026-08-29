class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores [temp, index] pairs
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append((temp, i))
        
        return res
        