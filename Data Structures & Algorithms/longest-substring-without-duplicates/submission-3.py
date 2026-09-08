class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set L as 0
        # new set
        # max counter

        # iterate thru s with R
            # while the current element exists in the set
                # get the new max counter with max
                # remove elem at L from set
                # advance L by 1
            # add curr elem to the set
        # do another get new max in case stuck inside

        L = 0
        substr_set = set()
        length_counter = 0

        for R in range(len(s)):
            while s[R] in substr_set:
                length_counter = max(length_counter, len(substr_set))
                substr_set.remove(s[L])
                L+=1
            substr_set.add(s[R])
            
        length_counter = max(length_counter, len(substr_set))
        return length_counter
                
