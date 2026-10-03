import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp_list = []

        for curr_token in tokens:
            if curr_token != "+" and curr_token != "-" and curr_token != "*" and curr_token != "/":
                tmp_list.append(int(curr_token))
            else:
                tmp_2 = tmp_list.pop()
                tmp_1 = tmp_list.pop()
                res = 0

                if curr_token == "+":
                    res = tmp_1 + tmp_2
                elif curr_token == "-":
                    res = tmp_1 - tmp_2
                elif curr_token == "*":
                    res = tmp_1 * tmp_2
                else:
                    res = math.trunc(tmp_1 / tmp_2)
                
                tmp_list.append(res)
        
        return tmp_list.pop()

