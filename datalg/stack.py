class Stack:
    def __init__(self):
        self._stack = []

    def __str__(self):
        return str(self._stack)

    def size(self):
        return len(self._stack)

    def empty(self):
        return self.size() == 0

    def peek(self):
        return self._stack[-1]

    def push(self, val):
        return self._stack.append(val)

    def pop(self):
        return self._stack.pop()
