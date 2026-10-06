class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding_str = ""
        for curr_str in strs:
            string_to_append = str(len(curr_str)) + "%" + curr_str
            encoding_str+=string_to_append
        # print(encoding_str)
        return encoding_str

    def decode(self, s: str) -> List[str]:
        res_arr = []

        i = 0
        prev_end = 0
        while i < len(s):
            if s[i] == "%":
                length = int(s[prev_end:i])
                stringer = s[i+1:i+length+1]
                res_arr.append(stringer)

                i, prev_end = i+length+1,i+length+1
            i+=1
        print(res_arr)
        return res_arr

                
                
        