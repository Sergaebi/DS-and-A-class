
# Problem 1
# -----------------------------------------------------------------


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


# Problem 2 and 3
# -----------------------------------------------------------------


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


# Deque with doubly linked list
class Deque:

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


# Problem 4
# -----------------------------------------------------------------


def divide_to_odd_and_even_linked_list(linked_list: DoubleLinkedList):
    odd_position_list = DoubleLinkedList()
    even_position_list = DoubleLinkedList()
    current_node = linked_list.get_first()
    while current_node is not None:
        even_position_list.insert_last(current_node.data)
        linked_list.remove(current_node.data)
        try:
            current_node = current_node.next.next
        except AttributeError:
            break
    current_node = linked_list.get_first()
    while current_node is not None:
        odd_position_list.insert_last(current_node.data)
        linked_list.remove(current_node.data)
        current_node = current_node.next
    return even_position_list, odd_position_list


# Problem 5 TESTING
# -----------------------------------------------------------------


def main():

    # TESTING PROBLEM 1
    # -----------------------------------------------------------------------------------------------------------

    print("TESTING Problem 1: CyclicDeque")
    deque = CyclicDeque()

    # testing add_first and add_last for CyclicDeque class
    # ----------------------------------------------------

    deque.insert_first(10)
    deque.insert_first(20)
    deque.insert_last(50)

    if deque.items == [20, 10, 50, None]:
        print("\n\tTesting add first and last for Cyclic Deque: PASS")
    else:
        print("\n\tTesting add first and last for Cyclic Deque: FAIL")

    print("\t", end="")
    print(deque)

    # testing delete first and last for CyclicDeque class
    # ----------------------------------------------------

    deque.deleteLast()
    deque.deleteFirst()

    if deque.items == [10, None, None, None]:
        print("\n\tTesting delete first and last for Cyclic Deque: PASS")
    else:
        print("\n\tTesting delete first and last for Cyclic Deque: FAIL")

    print("\t", end="")
    print(deque)

    # testing get first and last for CyclicDeque class
    # ----------------------------------------------------

    if deque.getFirst() == deque.getLast() == 10:
        print("\n\tTesting get first and last for Cyclic Deque: PASS")
    else:
        print("\n\tTesting get first and last for Cyclic Deque: FAIL")

    print("\t", end="")
    print(deque)

    # TESTING PROBLEM 2
    # -----------------------------------------------------------------------------------------------------------

    print("TESTING Problem 2: Deque with DoubleLinkedList")
    deque = Deque()

    # test that add_first and add_last functions
    # ----------------------------------------------------

    deque.add_first(1)
    deque.add_first("a")
    deque.add_last("b")
    deque.add_last("c")
    deque.add_first(4)

    if deque.get_first().data == 4 and deque.get_last().data == "c":
        print("\n\tInsert First/Last Test: PASS")
    else:
        print("\n\tInsert First/Last Test: FAIL")

    print("\t", end="")
    print(deque, end="")

    # test that removeFirst and removeLast functions
    # ----------------------------------------------------

    deque.remove_first()
    deque.remove_last()
    deque.remove_last()

    if deque.get_first().data == "a" and deque.get_last().data == 1:
        print("\tRemove First/Last Test: PASS")
    else:
        print("\tRemove First/Last Test: FAIL")

    print("\t", end="")
    print(deque, end="")

    # test get first, last, and size
    # ----------------------------------------------------

    if deque.items.size == deque.get_size():
        print("\tGet list size: PASS")
    else:
        print("\tGet list size: FAIL")

    if deque.items.first == deque.get_first():
        print("\n\tGet first size: PASS")
    else:
        print("\n\tGet first size: FAIL")

    if deque.items.last == deque.get_last():
        print("\n\tGet last size: PASS")
    else:
        print("\n\tGet last size: FAIL")

    # TESTING PROBLEM 3
    # -----------------------------------------------------------------------------------------------------------

    print("\nTESTING Problem 3: DoubleLinkedList")
    linked_list = DoubleLinkedList()

    # test that insertFirst and insertLast functions
    # ----------------------------------------------------

    linked_list.insert_first(1)
    linked_list.insert_first("a")
    linked_list.insert_last("b")
    linked_list.insert_last("c")
    linked_list.insert_first(4)

    if linked_list.get_first().data == 4 and linked_list.get_last().data == "c":
        print("\n\tInsert First/Last Test: PASS")
    else:
        print("\n\tInsert First/Last Test: FAIL")

    print("\t", end="")
    print(linked_list, end="")

    # test that remove_first and remove_last functions
    # ----------------------------------------------------

    linked_list.remove_first()
    linked_list.remove_last()
    linked_list.remove_last()

    if linked_list.get_first().data == "a" and linked_list.get_last().data == 1:
        print("\tRemove First/Last Test: PASS")
    else:
        print("\tRemove First/Last Test: FAIL")

    print("\t", end="")
    print(linked_list, end="")

    # test get first, last, and size
    # ----------------------------------------------------

    if linked_list.size == linked_list.get_size():
        print("\tGet list size: PASS")
    else:
        print("\tGet list size: FAIL")

    if linked_list.first == linked_list.get_first():
        print("\n\tGet first size: PASS")
    else:
        print("\n\tGet first size: FAIL")

    if linked_list.last == linked_list.get_last():
        print("\n\tGet last size: PASS")
    else:
        print("\n\tGet last size: FAIL")

    # test insert After and Before functions
    # ----------------------------------------------------

    linked_list.insert_after(4, "a")
    linked_list.insert_before("c", 4)

    current_node = linked_list.first
    list_to_check = []
    while current_node is not None:
        list_to_check.append(current_node.data)
        current_node = current_node.next
    if list_to_check == ["a", "c", 4, 1]:
        print("\n\tInsert Before After Test: PASS")
    else:
        print("\n\tInsert Before After Test: FAIl")

    print("\t", end="")
    print(linked_list, end="")

    # TESTING PROBLEM 4
    # -----------------------------------------------------------------------------------------------------------

    print("TESTING Problem 4: Even and Odd position\n")

    linked_list.insert_first(23)
    linked_list.insert_first(53)
    linked_list.insert_first(49)

    print("\t", end="")
    print("Old list before dividing : ", end="")
    print(linked_list, end="")

    even_position, odd_position = divide_to_odd_and_even_linked_list(linked_list)

    result = True

    current_node = even_position.first
    list_to_check = []
    while current_node is not None:
        list_to_check.append(current_node.data)
        current_node = current_node.next

    if list_to_check != [49, 23, 'c', 1]:
        result = False

    current_node = odd_position.first
    list_to_check = []
    while current_node is not None:
        list_to_check.append(current_node.data)
        current_node = current_node.next

    if list_to_check != [53, 'a', 4]:
        result = False

    if result:
        print("\n\tDivide to two lists at even and odd positions Test: PASS\n")
    else:
        print("\n\tDivide to two lists at even and odd positions Test: FAIL\n")

    print("\tEven position list: ", end="")
    print(even_position, end="")

    print("\tOdd position list: ", end="")
    print(odd_position, end="")


if __name__ == '__main__':
    main()
