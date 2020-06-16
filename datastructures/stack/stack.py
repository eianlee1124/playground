class Stack(object):

    def __init__(self):
        self.data = []

    def __repr__(self):
        return "Stack(%s)" % self.data

    def is_empty(self):
        return len(self.data) == 0
        
    def push(self, item):
        self.data.append(item)

    def pop(self, index=-1):
        value = self.data[index]
        del self.data[index]
        return value

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)
        
