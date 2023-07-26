class Stack:
    def __init__(self):
        self.st = []

    def is_empty(self):
        return len(self.st) == 0

    def push(self, item):
        self.st.append(item)

    def pop(self):
        if not self.is_empty():
            return self.st.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.st[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek an empty stack.")

    def size(self):
        return len(self.st)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.is_empty())
print(stack.size())
print(stack.pop())
print(stack.is_empty())
