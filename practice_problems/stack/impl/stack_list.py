class Stack:
    data = []

    def __init__(self, data=[]):
        for i in data:
            self.data.append(i)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.data.pop()
        raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.data) <= 0
