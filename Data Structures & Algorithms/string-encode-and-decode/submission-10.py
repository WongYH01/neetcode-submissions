class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for curr_string in strs:
            str_len = len(curr_string)
            format_str = str(str_len) + "%" + curr_string

            res_str+=format_str
        return res_str

    def decode(self, s: str) -> List[str]:
        # res array
        # 1st counter
        # 2nd counter

        # while 1st counter not at the end
            # check if 
        
        res_arr = []
        i = 0
        j = 0

        while i < len(s):
            curr_char = s[i]
            if curr_char == "%":
                str_len = int(s[j:i])
                j = i+str_len+1
                curr_str = s[i+1:j]
                res_arr.append(curr_str)
                i = j
            else:
                i+=1
        return res_arr
                
                
        