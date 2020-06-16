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

