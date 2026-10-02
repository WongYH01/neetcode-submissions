class MinStack:

    def __init__(self):
        self.stacker = []
        self.min_stacker = []

    def push(self, val: int) -> None:
        self.stacker.append(val)

        if not self.min_stacker or val <= self.min_stacker[-1]:
            self.min_stacker.append(val)

    def pop(self) -> None:
        popped_val = self.stacker.pop()
        if popped_val == self.min_stacker[-1]:
            self.min_stacker.pop()
        

    def top(self) -> int:
        return self.stacker[-1]
        

    def getMin(self) -> int:
        return self.min_stacker[-1]
