class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"( {self.data} )"


class LinkedList:

    def __init__(self, root=None):
        self.root: Node = root
        self.size = 0

    def add_beginning(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        current_node = self.root
        while current_node is not None:
            if current_node.data == data:
                return data
            else:
                current_node = current_node.next_node

    def remove(self, data):
        current_node = self.root
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next_node = current_node.next_node
                else:
                    self.root = current_node.next_node
                self.size -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        return False

    def reverseList(self):
        previous_node = None
        current_node = self.root
        while current_node is not None:
            next = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next
        self.root = previous_node

    def print_list(self):
        current_node = self.root
        while current_node is not None:
            print(current_node, end=" -> ")
            current_node = current_node.next_node


linked_list = LinkedList()
linked_list.add_beginning(4)
linked_list.add_beginning(76)
linked_list.add_beginning(3)
linked_list.add_beginning(0)
linked_list.add_beginning(1)

linked_list.print_list()
linked_list.reverseList()
print("\n")
linked_list.print_list()
