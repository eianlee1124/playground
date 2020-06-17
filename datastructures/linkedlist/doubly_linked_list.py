class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node(%s)" % self.data

    __str__ = __repr__


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.store = {}
        self.keys = self.store.keys()

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None
        self.store[new_node] = new_node.data

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        nodes.append("None")
        print(" -> ".join(map(str, nodes)))


