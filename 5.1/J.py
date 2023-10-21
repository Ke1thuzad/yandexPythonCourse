class Stack:
    def __init__(self):
        self.elems = []

    def push(self, item):
        self.elems.append(item)

    def pop(self):
        return self.elems.pop(-1)

    def is_empty(self):
        return False if len(self.elems) else True


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
