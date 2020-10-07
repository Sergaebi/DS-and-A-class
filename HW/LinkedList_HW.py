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
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

    # Please uncomment the block below and add the implementation of remaining functions

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
    def size(self):
        pass


class Node:
    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next = next_node
        self.previous = previous


class SingleLinkedList(ListADT):
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def insertFirst(self, obj):
        node = Node(obj, self._first)
        self._first = node
        if self._last is None:
            self._last = node
        self._size += 1

    def removeFirst(self):
        if self._first is None:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        self._first = self._first.next
        tmp.next = None
        self._size -= 1

    def insertLast(self, data):
        node = Node(data, None)
        if self._last is None:
            self._first = node
            self._last = node
            self._size += 1
            return
        self._last.next = node
        self._last = node
        self._size += 1

    def removeLast(self):
        if self._size == 0:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        # Iterate over the linked list to get a reference of the pre-last element
        while tmp.next != self._last:
            tmp = tmp.next

        tmp.next = None
        self._last = tmp
        self._size -= 1

    def size(self):
        return self._size

    def first(self):
        return self._first

    def last(self):
        return self._last

    # Implement the remaining functions of ListADT abstract class
    def insertBefore(self, data, data_to_check):
        if self._first and self._last:
            if self._first == self._last:
                self.insertFirst(data)
            else:
                current_node = self._first
                previous_node = None
                while current_node is not None:
                    if current_node.data == data_to_check:
                        new_node = Node(data, current_node)
                        if previous_node is None:
                            print(f"Now {data} is the root")
                            self._first = new_node
                        else:
                            previous_node.next = new_node
                        self._size += 1
                        return
                    else:
                        previous_node = current_node
                        current_node = current_node.next
        else:
            print("List is empty")
            self._first = Node(data, None)
            self._last = self._first
            self._size += 1

    def insertAfter(self, data, data_to_check):
        if self._first and self._last:
            if self._first == self._last:
                self.insertLast(data)
            else:
                current_node = self._first
                previous_node = None
                while current_node is not None:
                    if current_node.data == data_to_check:
                        new_node = Node(data, current_node.next)
                        if previous_node is None:
                            print(f"Now {data} is the root")
                            self._first = new_node
                        else:
                            current_node.next = new_node
                        self._size += 1
                        return
                    else:
                        previous_node = current_node
                        current_node = current_node.next
        else:
            print("List is empty")
            self._first = Node(data, None)
            self._last = self._first
            self._size += 1

    def remove(self, data):
        current_node = self._first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self._first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def indexOf(self, data):
        current_node = self._first
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
        self._first = root
        self._last = root
        self._size = 0
        if self._first is not None:
            self._size += 1

    def __len__(self):
        return self._size

    def insertFirst(self, data):
        if self._first and self._last:
            new_node = Node(data, self._first, None)
            self._first = new_node
            self._size += 1
        else:
            new_node = Node(data, None, None)
            self._first = new_node
            self._last = new_node

    def removeFirst(self):
        if self._first and self._last:
            self._first.next.previous = None
            self._first, self._first.next = self._first.next, None
        else:
            print("Nothing to remove")

    def insertLast(self, data):
        if self._first and self._last:
            new_node = Node(data, None, self._last)
            self._last = new_node
            self._size += 1
        else:
            new_node = Node(data, None, None)
            self._first = new_node
            self._last = new_node

    def removeLast(self):
        if self._first and self._last:
            self._last.previous.next = None
            self._last, self._last.previous = self._last.previous, None
        else:
            print("Nothing to remove")

    def first(self):
        return self._first

    def last(self):
        return self._last

    def size(self):
        return self._size

    def insertBefore(self, data, data_to_check):
        pass

    def insertAfter(self, data, data_to_check):
        pass

    def remove(self, data):
        current_node = self._first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self._first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def indexOf(self, data):
        current_node = self._first
        index = 0
        while current_node.next is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        print("No such data")

    # TODO Implement all functions of ListADT abstract class for double linked list


# This is an illustration of polymorphism, where the same printList function would be applicable to single linked list and double linked list objects due to common abstrct functions!
def printList(linked_list):
    print("Printing Linked List Elements")
    current = linked_list.first()
    while current is not None:
        print(str(current.data))
        current = current.next


# TODO implement a function for list collection which reverses the list
def reverseList(linked_list):
    pass


# TODO implement a function for list collection which updates the list through removing Numeric nodes
def removeNumericNodes(linked_list):
    pass


# TODO implement a function for list collection which updates the list through removing nodes at even positions
def removeNodesAtEvenPosition(linked_list):
    pass


# TODO implement a function which returns true if the the first element of the list is equel to the specified object and false if not
def testFirst(linked_list, obj):
    pass


# TODO implement a function which returns true if the the last element of the list is equel to the specified object and false if not
def testLast(linked_list, obj):
    pass


def testListFunctions(linked_list):
    linked_list.insertFirst(1)
    linked_list.insertFirst("a")
    linked_list.insertLast("b")
    linked_list.insertLast("c")
    linked_list.insertFirst(4)

    # test that insertFirst and insertLast functions work as expected
    # TODO substitute the code below with testFirst and testLast function calls
    if linked_list.first().data == 4 and linked_list.last().data == "c":
        print("Insert First/Last Test: PASS")
    else:
        print("Insert First/Last Test:FAIL")
    printList(linked_list)

    linked_list.removeFirst()
    linked_list.removeLast()
    linked_list.removeLast()
    # test that removeFirst and removeLast functions work as expected
    # TODO substitute the code below with testFirst and testLast function calls
    if linked_list.first().data == "a" and linked_list.last().data == 1:
        print("Remove First/Last Test:PASS")
    else:
        print("Remove First/Last Test:FAIL")
    printList(linked_list)

    linked_list.insertLast("b")
    linked_list.insertLast("c")
    linked_list.insertFirst(4)

    first = linked_list.first()
    last = linked_list.last()
    reverseList(linked_list)
    if first.data == linked_list.last().data and last.data == linked_list.last().data:
        print("Reverse List Test: PASS")
    else:
        print("Reverse List Test: FAIL")
    printList(linked_list)

    # TODO call newly implmented list functions and add tests for them as well similar to the above


sl = SingleLinkedList()
testListFunctions(sl)

# TODO Uncomment the code below after implementing the double linked list funcitons and make sure that all tests pass!
'''
dl = DoubleLinkedList()
testListFunctions(dl)
'''
