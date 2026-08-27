class MinStack:



    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if (len(self.min_stack) == 0) or (val <= self.min_stack[-1]):
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        remove_elem = self.stack[-1]
        if remove_elem == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
