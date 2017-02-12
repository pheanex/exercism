class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.first = self.last = None

    def push(self, element):
        if not self.last:
            self.last = self.first = Node(element)
        else:
            self.last = Node(element, prev=self.last)
            self.last.prev.next = self.last

    def pop(self):
        if not self.last:
            raise ValueError
        val = self.last.value
        self.last = self.last.prev
        if self.last:
            self.last.next = None
        return val

    def shift(self):
        if not self.first:
            raise ValueError
        val = self.first.value
        self.first = self.first.next
        if self.first:
            self.first.prev = None
        return val

    def unshift(self, element):
        if not self.first:
            self.last = self.first = Node(element)
        else:
            self.first = Node(element, next=self.first)
            self.first.next.prev = self.first
