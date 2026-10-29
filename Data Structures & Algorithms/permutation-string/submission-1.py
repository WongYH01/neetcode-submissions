class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0]*26
        s2_list = [0]*26

        L, limit = 0, len(s1)

        for char in s1:
            c_index = ord("a") - ord(char)
            s1_list[c_index] += 1
        
        for R in range(len(s2)):
            r_index = ord("a") - ord(s2[R])
            l_index = ord("a") - ord(s2[L])
            
            s2_list[r_index] += 1

            if (R-L+1) == limit:
                if s1_list == s2_list:
                    return True
                else:
                    s2_list[l_index] -= 1
                    L+=1
        return False