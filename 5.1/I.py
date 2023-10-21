class Queue:
    def __init__(self):
        self.elems = []

    def push(self, item):
        self.elems.append(item)

    def pop(self):
        return self.elems.pop(0)

    def is_empty(self):
        return False if len(self.elems) else True
