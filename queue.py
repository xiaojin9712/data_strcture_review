class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def size(self):
        return len(self.items)