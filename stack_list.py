class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        if len(self.stack) <5:
            self.stack.append(data)
        else: 
            print("OverFlow")
            return
    def pop(self):
        if len(self.stack) == 0:
            print("Stack underflow")
            return
        else:
            self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        print(self.stack[-1])
    def display(self):
        print(self.stack)
s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.push(25)
# s.push(30)