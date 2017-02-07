import queue


class CircularBuffer:
    def __init__(self, size):
        self.queue = queue.Queue(size)

    def read(self):
        if self.queue.empty():
            raise BufferEmptyException
        return self.queue.get()

    def write(self, element):
        if not self.queue.full():
            self.queue.put(element)
        else:
            raise BufferFullException

    def overwrite(self, element):
        if self.queue.full():
            self.queue.get()
        self.queue.put(element)

    def clear(self):
        while not self.queue.empty():
            self.queue.get()


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass
