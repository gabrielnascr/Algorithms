"""
    A stack is a data structure that allows removing elements and insert new objects.
    More specifically, the stack a structure subject to the following operating 
    rule: whenever there is a removal, 
    the removed element is the one that has been in the structure for the last time 
"""

class Stack:

    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, element):
        self.stack.append(element)
        self.len+= 1

    def pop(self):
        self.stack.pop(self.len - 1)
        self.len-= 1

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return self.len

stack = Stack()

stack.push(1)
print(stack.top())