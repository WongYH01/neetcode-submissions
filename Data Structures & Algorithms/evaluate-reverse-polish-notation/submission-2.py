import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buffer_stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                buffer_stack.append(int(token))
            else:
                second_num = buffer_stack.pop()
                first_num = buffer_stack.pop()
                inter_num = 0
                if token == "+":
                    inter_num = first_num + second_num
                if token == "*":
                    inter_num = first_num * second_num
                if token == "-":
                    inter_num = first_num - second_num
                if token == "/":
                    inter_num = math.trunc(first_num/second_num)
                buffer_stack.append(inter_num)
        return buffer_stack.pop()
