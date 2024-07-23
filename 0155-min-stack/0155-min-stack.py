class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minVal:
            self.minVal = val
        self.minStack.append(self.minVal)
 

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if len(self.stack) ==0 and len(self.minStack) ==0:
            self.minVal = float('inf')
        else:
            self.minVal = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()