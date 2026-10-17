#stack is a linear data structure which contain only one opening so, the insertion and deletion of data will happen in same end 
#stack follow LIFO methodology there is a pointer called top which points to the top of the stack 
#top will be initialized with -1 in array implementation 
#And it will be initialized with the null value in a linked list implementation 
class Stack:
    SIZE = 100

    def __init__(self):
        self.stack = [0]*self.SIZE
        self.top = -1

    def isFull(self):
        return self.top == self.SIZE-1
    def isEmpty(self):
            return self.top == -1
    def push(self,val):
        if self.isFull():
            print("Stack overflow")
            return
        self.top+=1
        self.stack[self.top] = val

    def pop(self):
        if self.isEmpty():
            print("Stack is Underflow")
            return
        x = self.stack[self.top]
        self.top-=1
        return x

    def peek(self):
        if self.isEmpty():
                    print("Stack is Empty")
                    return -1
        return self.stack[self.top]


    def display(self):
        if self.isEmpty():
              print("Stack is Empty")
              return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=" ")
        print()

s = Stack()
while True:
    value = int(input())
    if value == -1:
         break
    s.push(value)

s.display()