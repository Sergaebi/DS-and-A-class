class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "(" + str(self.data, self.next_node) + ")"


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

    def print_list(self):
        current_node = self.root
        while current_node is not None:
            print(current_node, end="->")
            current_node = current_node.next_node
