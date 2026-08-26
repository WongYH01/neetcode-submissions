class Solution:
    def isValid(self, s: str) -> bool:
        buffer_stack = []
        ref_dict = {"(":")","[":"]","{":"}"}

        for char in s:
            if char in ref_dict:
                buffer_stack.append(char)
            else:
                if len(buffer_stack) == 0 or char != ref_dict[buffer_stack[-1]]:
                    return False
                if char == ref_dict[buffer_stack[-1]]:
                    buffer_stack.pop()

        if len(buffer_stack) == 0:
            return True
        return False
