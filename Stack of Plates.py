class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            return None
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return value


# Example usage:
stacks = SetOfStacks(3)  # Each sub-stack has a capacity of 3

# Push values onto the stack
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)

# Pop values from the stack
print(stacks.pop())  # Output: 5
print(stacks.pop())  # Output: 4

# Pop value from a specific stack
print(stacks.popAt(0))  # Output: 3 (from the first stack)
