from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insertFirst(self, data):
        pass

    @abstractmethod
    def removeFirst(self):
        pass

    @abstractmethod
    def insertLast(self, data):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_last(self):
        pass

    @abstractmethod
    def insertBefore(self, data, data_to_check):
        pass

    @abstractmethod
    def insertAfter(self, data, data_to_check):
        pass

    @abstractmethod
    def remove(self, data):
        pass

    @abstractmethod
    def indexOf(self, data):
        pass

    @abstractmethod
    def get_size(self):
        pass


class Node:

    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next = next_node
        self.previous = previous


class SingleLinkedList(ListADT):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insertFirst(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    def removeFirst(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def insertLast(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def removeLast(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        while tmp.next != self.last:
            tmp = tmp.next
        tmp.next = None
        self.last = tmp
        self.size -= 1

    def get_size(self):
        return self.size

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def insertBefore(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            previous_node = None
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node)
                    if previous_node is None:
                        self.first = new_node
                    else:
                        previous_node.next = new_node
                    self.size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
        else:
            print("List is empty")

    def insertAfter(self, data, data_to_check):
        if self.first and self.last:
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node.next)
                    if current_node.next is None:
                        current_node.next = new_node
                        self.last = new_node
                    else:
                        current_node.next = new_node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
        else:
            print("List is empty")

    def remove(self, data):
        current_node = self.first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def indexOf(self, data):
        current_node = self.first
        index = 0
        while current_node.next is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        print("No such data")


class DoubleLinkedList(ListADT):

    def __init__(self, root=None):
        self.first = root
        self.last = root
        self.size = 0
        if self.first is not None:
            self.size += 1

    def insertFirst(self, data):
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

    def removeFirst(self):
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

    def insertLast(self, data):
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

    def removeLast(self):
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

    def insertBefore(self, data, data_to_check):
        if self.first and self.last:
            previous_node = None
            current_node = self.first
            while current_node is not None:
                if current_node.data == data_to_check:
                    new_node = Node(data, current_node, previous_node)
                    if previous_node is None:
                        self.first.previous = new_node
                        self.first = new_node
                    else:
                        previous_node.next = new_node
                        current_node.next.previous = new_node
                    self.size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
            print("Nothing to insert after")
            return
        else:
            print("List is empty")

    def insertAfter(self, data, data_to_check):
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
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def indexOf(self, data):
        current_node = self.first
        index = 0
        while current_node.next is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        print("No such data")


def printList(linked_list):
    print("Printing Linked List Elements")
    current = linked_list.get_first()
    if isinstance(linked_list, SingleLinkedList):
        while current is not None:
            print(f"( {current.data} ) -> ", end="")
            current = current.next
        print("None")
    else:
        print("None -> ", end="")
        while current is not None:
            print(f" <- ( {current.data} ) -> ", end="")
            current = current.next
        print(" <- None")
    print()
