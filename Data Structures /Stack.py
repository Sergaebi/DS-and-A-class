class Stack:

    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return self.stack

