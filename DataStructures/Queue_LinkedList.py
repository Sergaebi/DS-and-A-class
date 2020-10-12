class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class QueueLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.__size = 0

    def enqueue(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.__size += 1
            return
        self.last.next = node
        self.last = node
        self.__size += 1

    def dequeue(self):
        if self.first is None:
            return
        if self.__size == 1:
            self.first = None
            self.last = None
            self.__size -= 1
            return
        temporary = self.first
        self.first = self.first.next
        temporary.next = None
        self.__size -= 1

    def is_empty(self):
        return self.__size == 0

    def empty_queue(self):
        self.__size = 0
        self.first = None
        self.last = None

    def get_size(self):
        return self.__size

    size = property(get_size)


queue = QueueLinkedList()
print(queue.size)
