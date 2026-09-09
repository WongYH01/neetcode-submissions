class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # L as 0
        # dictionary
        # max length
        
        # iterate through string with s
            # check if R elem does not exist in dict
                # create one with counter of 0
            # add to the dict according to R increment counter by 1

            # while the dictionary is not empty and k - max of the values is > k
                # reduce counter of [L] key by 1
                # move L by 1
            
            # compare and get max length
        
        L = 0
        counter_dict = {}
        max_length = 0

        for R in range(len(s)):

            if s[R] not in counter_dict:
                counter_dict[s[R]] = 0
            counter_dict[s[R]]+=1

            
            while counter_dict and ((R-L+1)-max(counter_dict.values()) > k):
                counter_dict[s[L]]-=1
                L+=1

            max_length = max(max_length,R-L+1)

        return max_length
