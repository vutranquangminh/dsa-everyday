class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        arr = []
        minimum = self.stack[-1]

        while len(self.stack):
            minimum = min(minimum, self.stack[-1])
            arr.append(self.stack.pop())
        
        while len(arr):
            self.stack.append(arr.pop())
        
        return minimum