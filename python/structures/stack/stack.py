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

    #Insert an element into the stack
    def push(self, e):
        self.stack.append(e)
        self.len += 1

    # Remove the last element into the stack
    def pop(self):
        if self.len > 0:
            self.stack.pop(self.len - 1)
            self.len -= 1
        raise IndexError("This stack is empty")

    # return the top
    def peek(self):
        if self.len > 0:
            return self.stack[-1]
        raise IndexError("This stack is empty")

    # return the stack length
    def __len__(self):
        return self.len


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(7)
stack.push(8)

print(len(stack))
print(stack.peek())
