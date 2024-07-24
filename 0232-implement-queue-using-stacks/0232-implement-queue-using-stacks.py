class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
        # print(self.stack1)


    def pop(self) -> int:
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        # print(self.stack2)
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
             
        return self.stack2[-1]
        

    def empty(self) -> bool:
        if self.stack1 == [] and self.stack2 == []:
            return True
        
 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()