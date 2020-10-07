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

    # DONE TESTING
    def insertFirst(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
    def get_size(self):
        return self.size

    # DONE TESTING
    def get_first(self):
        return self.first

    # DONE TESTING
    def get_last(self):
        return self.last

    def insertBefore(self, data, data_to_check):
        if self.first and self.last:
            if self.first == self.last:
                self.insertFirst(data)
            else:
                current_node = self.first
                previous_node = None
                while current_node is not None:
                    if current_node.data == data_to_check:
                        new_node = Node(data, current_node)
                        if previous_node is None:
                            print(f"Now {data} is the root")
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
            self.first = Node(data, None)
            self.last = self.first
            self.size += 1

    def insertAfter(self, data, data_to_check):
        if self.first and self.last:
            if self.first == self.last:
                self.insertLast(data)
            else:
                current_node = self.first
                previous_node = None
                while current_node is not None:
                    if current_node.data == data_to_check:
                        new_node = Node(data, current_node.next)
                        if previous_node is None:
                            print(f"Now {data} is the root")
                            self.first = new_node
                        else:
                            current_node.next = new_node
                        self.size += 1
                        return
                    else:
                        previous_node = current_node
                        current_node = current_node.next
        else:
            print("List is empty")
            self.first = Node(data, None)
            self.last = self.first
            self.size += 1

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE TESTING
    def get_first(self):
        return self.first

    # DONE TESTING
    def get_last(self):
        return self.last

    def get_size(self):
        return self.size

    def insertBefore(self, data, data_to_check):
        pass

    def insertAfter(self, data, data_to_check):
        pass

    # DONE TESTING
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

    # DONE TESTING
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

    # DONE Implement all functions of ListADT abstract class for double linked list


def printList(linked_list):
    print("Printing Linked List Elements")
    current = linked_list.get_first()
    while current is not None:
        print(str(current.data))
        current = current.next


# DONE implement a function for list collection which reverses the list
def reverseList(linked_list: SingleLinkedList):
    previous_node = None
    current_node = linked_list.first
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    linked_list.first = previous_node
    current_node = linked_list.first
    while current_node.next is not None:
        current_node = current_node.next
    linked_list.last = current_node


# DONE implement a function for list collection which updates the list through removing Numeric nodes
def removeNumericNodes(linked_list: SingleLinkedList):
    current_node = linked_list.get_first()
    while current_node is not None:
        if isinstance(current_node.data, int) or isinstance(current_node.data, float):
            linked_list.remove(current_node.data)
        current_node = current_node.next


# DONE implement a function for list collection which updates the list through removing nodes at even positions
def removeNodesAtEvenPosition(linked_list):
    current_node = linked_list.first.next
    while current_node is not None:
        linked_list.remove(current_node.data)
        try:
            current_node = current_node.next.next
        except AttributeError:
            return


# DONE implement a function which returns true if the the first element of the list is equal to the specified object and false if not
def testFirst(linked_list, data):
    if linked_list.first.data == data:
        return True
    return False


# DONE implement a function which returns true if the the last element of the list is equal to the specified object and false if not
def testLast(linked_list, data):
    if linked_list.last.data == data:
        return True
    return False


def testListFunctions(linked_list):

    # test that insertFirst and insertLast functions work as expected
    # DONE substitute the code below with testFirst and testLast function calls
    # ---------------------------------------------------------------------------------------

    linked_list.insertFirst(1)
    linked_list.insertFirst("a")
    linked_list.insertLast("b")
    linked_list.insertLast("c")
    linked_list.insertFirst(4)

    if linked_list.get_first().data == 4 and linked_list.get_last().data == "c":
        print("\nInsert First/Last Test: PASS")
    else:
        print("\nInsert First/Last Test: FAIL")

    printList(linked_list)

    # test that removeFirst and removeLast functions work as expected
    # DONE substitute the code below with testFirst and testLast function calls
    # ---------------------------------------------------------------------------------------

    linked_list.removeFirst()
    linked_list.removeLast()
    linked_list.removeLast()

    if linked_list.get_first().data == "a" and linked_list.get_last().data == 1:
        print("\nRemove First/Last Test: PASS")
    else:
        print("\nRemove First/Last Test: FAIL")

    printList(linked_list)

    # test get first, last, and size
    # DONE
    # ---------------------------------------------------------------------------------------

    if linked_list.size == linked_list.get_size():
        print("\nGet list size: PASS")
    else:
        print("\nGet list size: FAIL")

    if linked_list.first == linked_list.get_first():
        print("\nGet first size: PASS")
    else:
        print("\nGet first size: FAIL")

    if linked_list.last == linked_list.get_last():
        print("\nGet last size: PASS")
    else:
        print("\nGet last size: FAIL")

    # test remove function
    # DONE
    # ---------------------------------------------------------------------------------------

    linked_list.insertLast("c")
    linked_list.insertFirst(4)

    current_node = linked_list.first
    list_to_check = []
    while current_node is not None:
        list_to_check.append(current_node.data)
        current_node = current_node.next
    if list_to_check == [4, "a", 1, "c"]:
        print("\nRemove Test: PASS")
    else:
        print("\nRemove Test: FAIl")
    printList(linked_list)

    # test indexOf function
    # DONE
    # ---------------------------------------------------------------------------------------

    if linked_list.indexOf(1) == 2:
        print("\nIndex function Test: PASS")
    else:
        print("\nIndex function: FAIl")

    # test reverseList function
    # DONE
    # ---------------------------------------------------------------------------------------

    linked_list.insertLast("b")
    linked_list.insertLast("c")
    linked_list.insertFirst(4)

    first = linked_list.get_first().data
    last = linked_list.get_last().data

    reverseList(linked_list)

    if first == linked_list.get_last().data and last == linked_list.get_first().data:
        print("\nReverse List Test: PASS")
    else:
        print("\nReverse List Test: FAIL")
    printList(linked_list)

    # test removeNumericNodes function
    # DONE
    # ---------------------------------------------------------------------------------------

    removeNodesAtEvenPosition(linked_list)

    current_node = linked_list.first
    list_to_check = []
    while current_node is not None:
        list_to_check.append(current_node.data)
        current_node = current_node.next
    if list_to_check == ["c", "c", "a", 4]:
        print("\nRemove at even position Test: PASS")
    else:
        print("\nRemove at even position Test: FAIl")
    printList(linked_list)

    # test removeNumericNodes function
    # DONE
    # ---------------------------------------------------------------------------------------

    removeNumericNodes(linked_list)

    current_node = linked_list.first
    check = True
    while current_node is not None:
        if isinstance(current_node.data, int) or isinstance(current_node.data, float):
            print("\nRemove numeric values Test: FAIL")
            check = False
            break
        current_node = current_node.next
    if check:
        print("\nRemove numeric values Test: PASS")
    printList(linked_list)
    # DONE call newly implemented list functions and add tests for them as well similar to the above


sl = SingleLinkedList()
testListFunctions(sl)

print("\n---------------------------------------------------------------------------------------")

dl = DoubleLinkedList()
testListFunctions(dl)
