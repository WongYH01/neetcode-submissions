class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        res_array = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if temp_stack:
                while temp_stack and temperatures[i]>temperatures[temp_stack[-1]]:
                    prev_index = temp_stack.pop()
                    res_array[prev_index] = i - prev_index
            temp_stack.append(i)
        return res_array
        