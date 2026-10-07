class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set L as 0
        # a set 

        L = 0
        sub_set = set()
        max_count = 0

        for R in range(len(s)):
            curr_elem = s[R]
            while curr_elem in sub_set:
                curr_length = R-L
                max_count = max(max_count,curr_length)

                sub_set.remove(s[L])
                L+=1
            sub_set.add(curr_elem)

            max_count = max(max_count, len(sub_set))
        return max_count