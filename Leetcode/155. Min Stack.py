class MinStack:
    stack = None
    min_stack = None
    top_i = None
    min = None

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_i = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min = val
        self.min_stack.append(self.min)
        self.min = min(self.min, val)
        self.top_i += 1

    def pop(self) -> None:
        stk_top = self.stack.pop()
        min_stk_top = self.min_stack.pop()
        self.min = min_stk_top
        self.top_i -= 1

    def top(self) -> int:
        return self.stack[self.top_i - 1]

    def getMin(self) -> int:
        return self.min