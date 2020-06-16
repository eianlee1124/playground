def is_empty(attr):
    return len(attr) > 0

def is_full(obj):
    return obj.qsize == obj.maxsize


class Queue(object):

    def __init__(self, maxsize=None):
        if maxsize is not None:
            if maxsize < 0:
                raise ValueError
        self.maxsize = maxsize
        self.stack1 = []
        self.stack2 = []
        
    @property
    def qsize(self):
        return len(self.stack1) + len(self.stack2)

    def put(self, elem):
        if is_full(self):
            raise IndexError
        self.stack1.append(elem)

    def get(self):
        if not self.qsize:
            raise IndexError
        if not is_empty(self.stack2):
            while is_empty(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

