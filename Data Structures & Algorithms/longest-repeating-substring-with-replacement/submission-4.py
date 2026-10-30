class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap
        # L as 0

        # iterate with R
            # check if char exists
                # new key of val 0
            # add the pointer

            # get curr length
            # check if got more than 1 keys in hashmap
                # check if k 
        
        counter_map = {}
        L = 0
        max_len = 0

        for R in range(len(s)):
            if s[R] not in counter_map:
                counter_map[s[R]] = 0
            counter_map[s[R]] += 1

            while len(counter_map) > 1 and (R-L+1 - max(counter_map.values())) > k:
                counter_map[s[L]] -= 1
                L+=1
        
            max_len = max(max_len,R-L+1)

        return max_len



