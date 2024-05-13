class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Stack to keep track of minimum elements

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
print(stack.getMin())  # Output: 2
stack.pop()
print(stack.top())  # Output: 5
print(stack.getMin())  # Output: 3
