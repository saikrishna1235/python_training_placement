class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def precedence(self, ch):
        if ch == "*" or ch == "/":
            return 2
        if ch == "+" or ch == "-":
            return 1
        return 0

    def postfixExp(self, exp):
        postfix = ""
        for i in exp:
            # 1. If the character is an operand, add it to the output
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or i.isdigit():
                postfix += i
            
            # 2. If the character is '(', push it to the stack
            elif i == '(':
                self.push(i)
            
            # 3. If the character is ')', pop until '(' is found
            elif i == ')':
                while not self.is_empty() and self.peek() != '(':
                    postfix += self.pop()
                self.pop()  # Pop the '(' off the stack
            
            # 4. If an operator is encountered
            else:
                while (not self.is_empty() and 
                       self.precedence(self.peek()) >= self.precedence(i)):
                    postfix += self.pop()
                self.push(i)

        # Pop all the remaining operators from the stack
        while not self.is_empty():
            postfix += self.pop()
            
        return postfix

# Example Usage:
s = Stack()
expression = "a+b*(c^d-e)^(f+g*h)-i"
print(s.postfixExp("a+b*c"))  # Output: abc*+
print(s.postfixExp("(a+b)*c")) # Output: ab+c*
