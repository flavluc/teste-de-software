class Queue:
    def __init__(self):
        self._queue = []

    def __str__(self):
        return str(self._queue)

    def size(self):
        return len(self._queue)

    def empty(self):
        return self.size() == 0

    def front(self):
        return self._queue[0]

    def enqueue(self, val):
        return self._queue.append(val)

    def dequeue(self):
        return self._queue.pop(0)
