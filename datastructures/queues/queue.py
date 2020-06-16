class Full(Exception):
    pass

class Empty(Exception):
    pass

class Queue(object):

    def __init__(self, maxsize=10):
        if not isinstance(maxsize, int):
            if maxsize < 0:
                raise ValueError

        self.maxsize = maxsize
        self.stack = [None] * maxsize
        self.front = 0
        self.rear = 0
        self.size = 0

    def __iter__(self):
        pos = self.front
        while True:
            if pos == self.rear:
                return
            yield self.stack[pos]
            pos += 1

    def __repr__(self):
        return "Queue([%s])" % self.stack[:self.size]

    def is_empty(self):
        return self.size == 0

    def put(self, item):
        if self.rear == len(self.stack):
            raise Full("Maximum occupancy has been reached")
        self.stack[self.rear] = item
        self.rear += 1
        self.size += 1

    def get(self):
        if self.is_empty():
            raise Empty("Pop from empty queue")
        value = self.stack[self.front]
        self.stack[self.front] = None
        self.front += 1
        self.size -= 1
        return value
