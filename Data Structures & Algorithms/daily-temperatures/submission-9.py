class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # intermediate stack
        # res array of 0s * len(temp)
        # iterate thru list of temps with i
            # check if stack empty
                # push into stack
            # else
                # while the top of the stack is smaller than current temp
                    # get the index with pop
                    # change the res_array index to the diff between curr index and got index
                # push into stack

        temp_stack = []
        res_array = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while temp_stack and (temp_stack[-1][0] < temperatures[i]):
                    prev_temp,prev_index = temp_stack.pop()
                    res_array[prev_index] = i - prev_index
            struct = [temperatures[i],i]
            temp_stack.append(struct)
        return res_array