class CyclicDeque:

    def __init__(self):
        self.items = [None]
        self.size = 0

    def double_size(self):
        new_size = len(self.items) * 2
        new_items = []
        for i in range(new_size):
            new_items.append(None)
        for item in range(len(self.items)):
            new_items[item] = self.items[item]
        self.items = new_items

    def is_full(self):
        if self.size == len(self.items):
            return True
        return False

    def is_empty(self):
        return self.size == 0

    def insert_first(self, data):
        if self.is_full():
            self.double_size()
        if self.items[0] is None:
            self.items[0] = data
            self.size += 1
        else:
            if self.items[-1] is None:
                self.items.pop(-1)
                self.items.insert(0, data)
                self.size += 1

    def insert_last(self, data):
        if self.is_full():
            self.double_size()
        self.items[self.size] = data
        self.size += 1

    def deleteFirst(self):
        self.items.pop(0)
        self.items.append(None)
        self.size -= 1

    def deleteLast(self):
        self.items[self.size - 1] = None
        self.size -= 1

    def getFirst(self):
        return self.items[0]

    def getLast(self):
        return self.items[self.size - 1]

    def __repr__(self):
        print("Printing Cyclic Deque: ", end="\t")
        print(self.items)
        return ""


class Node:

    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next: Node = next_node
        self.previous = previous


class DoubleLinkedList:

    def __init__(self, root=None):
        self.first = root
        self.last = root
        self.size = 0
        if self.first is not None:
            self.size += 1

    def insert_first(self, data):
        if self.first and self.last:
            new_node = Node(data, self.first, None)
            self.first.previous = new_node
            if self.first == self.last:
                self.last.previous = new_node
            self.first = new_node
            self.size += 1
        else:
            new_node = Node(data, None, None)
            self.first = new_node
            self.last = new_node
        return new_node

    def remove_first(self):
        if self.first and self.last:
            if self.first == self.last:
                self.first = None
                self.last = None
                self.size -= 1
            else:
                self.first.next.previous = None
                temporary = self.first
                self.first = self.first.next
                temporary.next = None
                self.size -= 1
        else:
            print("Nothing to remove")

    def insert_last(self, data):
        if self.first and self.last:
            new_node = Node(data, None, self.last)
            self.last.next = new_node
            if self.first == self.last:
                self.first.next = new_node
            self.last = new_node
            self.size += 1
        else:
            new_node = Node(data, None, None)
            self.first = new_node
            self.last = new_node
        return new_node

    def remove_last(self):
        if self.first and self.last:
            if self.first == self.last:
                self.first = None
                self.last = None
                self.size -= 1
            else:
                self.last.previous.next = None
                temporary = self.last
                self.last = self.last.previous
                temporary.previous = None
                self.size -= 1
        else:
            print("Nothing to remove")

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_size(self):
        return self.size

    def insert_before(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node, current_node.previous)
                    if current_node.previous is None:
                        self.first.previous = new_node
                        self.first = new_node
                    else:
                        current_node.previous.next = new_node
                        current_node.previous = new_node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
            print("Nothing to insert after")
            return
        else:
            print("List is empty")

    def insert_after(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node.next, current_node)
                    if current_node.next is None:
                        current_node.next = new_node
                    else:
                        current_node.next.previous = new_node
                        current_node.next = new_node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
            print("Nothing to insert after")
            return
        else:
            print("List is empty")

    def remove(self, data):
        current_node = self.first
        while current_node is not None:
            if current_node.data == data:
                if current_node.previous is not None:
                    current_node.previous.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                current_node = current_node.next

    def __repr__(self):
        print("Printing Linked List Elements: ", end="")
        current = self.get_first()
        print("None -> ", end="")
        while current is not None:
            print(f" <- ( {current.data} ) -> ", end="")
            current = current.next
        print(" <- None")
        print()
        return ""


class DequeWithDoubleLinkedList:

    def __init__(self):
        self.items = DoubleLinkedList()
        self.capacity = 8

    def add_first(self, data):
        if self.is_full():
            print("Overload!")
            return
        self.items.insert_first(data)

    def add_last(self, data):
        if self.is_full():
            print("Overload!")
            return
        self.items.insert_last(data)

    def remove_first(self):
        self.items.remove_first()

    def remove_last(self):
        self.items.remove_last()

    def get_first(self):
        return self.items.get_first()

    def get_last(self):
        return self.items.get_last()

    def is_full(self):
        return self.items.get_size() == 8

    def get_size(self):
        return self.items.get_size()

    def __repr__(self):
        current_node = self.items.get_first()
        deque = []
        while current_node is not None:
            deque.append(current_node.data)
            current_node = current_node.next
        return "Printing Deque: " + str(deque) + "\n\n"
