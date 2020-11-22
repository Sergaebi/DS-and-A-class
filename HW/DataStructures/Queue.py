class Queue:

    def __init__(self) -> None:
        self.queue: list = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def __repr__(self):
        return self.queue
