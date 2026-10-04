class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res list
        # iterate to temperatures
            # append 0 to res list
        # temp stack
        # iterate thru temperatures with i
            # check if the curr temp is bigger than the top of the stack
                # while the curr temp is bigger than top of stack
                    # pop it
                    # take the diff between popped index and curr index
                    # change the value w/ in popped index to the diff
            # add [val, index] to the stack
        # return res list

        res_list = []
        for j in range(len(temperatures)):
            res_list.append(0)
        tmp_stack = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            if tmp_stack:
                while tmp_stack and curr_temp > tmp_stack[-1][0]:
                    popped_ting = tmp_stack.pop()
                    popped_temp, popped_index = popped_ting[0],popped_ting[1]
                    diff_length = i-popped_index
                    res_list[popped_index] =  diff_length
            tmp_stack.append([temperatures[i],i])
        return res_list