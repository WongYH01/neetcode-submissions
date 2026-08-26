class Solution:
    def isValid(self, s: str) -> bool:
        # empty buffer stack
        # reference dict

        # iterate thru string
            # if curr char in dict (is opening)
                # push into buffer dict
            # else (is closing)
                # if buffer stack empty or the stack's latest is not the closing's opening
                    # return False
                # 

        buffer_stack = []
        ref_dict = {"(":")","[":"]","{":"}"}

        for char in s:
            if char in ref_dict:
                buffer_stack.append(char)
            else:
                if len(buffer_stack) == 0 or char != ref_dict[buffer_stack[-1]]:
                    return False
                buffer_stack.pop()

        if len(buffer_stack) == 0:
            return True
        return False
