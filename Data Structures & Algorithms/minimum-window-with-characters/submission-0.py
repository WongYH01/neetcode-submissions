class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # iterate thru t
            # turn it into the t_dict
        # set need counter to be length of t_dict

        # set res length to be length of s + 1
        # res coordinate
        # set L as 0
        # iterate thru s with R:
            # check if R elem exists in s_dict
                # create new key with 0
            # add the R elem to s_dict
            # check if R elem in t_dict
                # check if the current count is == the ref count
                    # up the have counter

            # while the have counter is the same as the need counter
                # check if the current window is smaller than res_length
                    # change accordingly
                # remove the L element from s_dict
                # check if the L elem exists in t_dict
                    # check if the value from s_dict is smaller than t_dict
                        # down the have counter
                # move L by 1
        t_dict = {}
        for t_char in t:
            if t_char not in t_dict:
                t_dict[t_char] = 0
            t_dict[t_char]+=1
        t_counter = len(t_dict)

        res_length = len(s)+1
        res_start, res_end = 0,0
        
        L = 0
        s_dict = {}
        s_counter = 0
        for R in range(len(s)):
            if s[R] not in s_dict:
                s_dict[s[R]] = 0
            s_dict[s[R]] += 1

            if s[R] in t_dict and s_dict[s[R]] == t_dict[s[R]]:
                s_counter += 1
            
            while s_counter == t_counter:
                if (R-L+1) < res_length:
                    res_length = (R-L+1)
                    res_start, res_end = L,R
                
                s_dict[s[L]] -= 1
                if s[L] in t_dict:
                    if s_dict[s[L]] < t_dict[s[L]]:
                        s_counter -= 1
                L += 1

        if res_length == len(s)+1:
            return ""
        else:
            return s[res_start:res_end+1]
