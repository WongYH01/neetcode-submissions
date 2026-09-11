class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get length of s1 as window

        # L = 0
        # create an array with 26 0s

        # check is s1 bigger than s2
            # return false
        
        # convert s1 to bucket sort

        # get the window size with len(s1)
        # iterate thru s2 with R
            # check if the current length is bigger than k
                # down the array count with the elem alpha index
                # move L by 1
            # add elem R the index with ord
            # if the arrays are the same
                # return true
        # return false

        if len(s1) > len(s2):
            return False
        
        s1_array = [0]*26
        s2_sliding_array = [0]*26

        for curr_char in s1:
            s1_array[ord('a')-ord(curr_char)] += 1
        
        L = 0
        k = len(s1)

        for R in range(len(s2)):
            if R-L+1 > k:
                s2_sliding_array[ord('a')-ord(s2[L])]-=1
                L+=1
            s2_sliding_array[ord('a')-ord(s2[R])]+=1

            if s2_sliding_array == s1_array:
                return True
        return False
        
        