try:
    from _collections import deque
except ImportError:
    from collections import deque

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node(%s)" % self.data

    __str__ = __repr__

class SinglyLinkedList(object):

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            nodes = deque(nodes)
            node = Node(nodes.popleft())
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(str(curr))
            curr = curr.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        for current_node in self:
            pass
        current_node.next = new_node

    def appendleft(self, new_node):
        curr = Node(new_node)
        curr.next = self.head
        self.head = curr

    def insert_next(self, target, new_node):
        if self.head is None:
            raise IndexError("Insert from empty list")

        new_node = Node(new_node) 
        for curr in self:
            if curr.data is target:
                new_node.next = curr.next
                curr.next = new_node
                return
        raise IndexError(f"Node {target} not found")

    def insert_prev(self, target, new_node):
        if self.head is None:
            raise IndexError("Insert from empty list")
        if self.head.data is target:
            self.appendleft(Node(new_node))
        
        prev = self.head
        new_node = Node(new_node)
        for curr in self:
            if curr.data is target:
                prev.next = new_node
                new_node.next = curr
                return
            prev = curr
        raise IndexError(f"Node {target} not found")

    def remove(self, target):
        if self.head is None:
            raise ValueError(f"{target} not in list")
        if self.head.data is target:
            self.head = self.head.next
            return
        prev = self.head
        for curr in self:
            if curr.data is target:
                prev.next = curr.next
                return
            prev = curr
        raise ValueError(f"{target} not in list")
