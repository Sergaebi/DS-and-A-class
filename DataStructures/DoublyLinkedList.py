class Node:

    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node: Node = next_node
        self.previous_node: Node = previous_node

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self, root):
        self.root: Node = root
        self.last: Node = root
        self.size = 0
        if self.root is not None:
            self.size += 1

    def __len__(self):
        return self.size

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.last = self.root
        else:
            new_node = Node(data)
            self.root.previous_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        current_node: Node = self.root
        while current_node is not None:
            if current_node.data == data:
                return data
            elif current_node.next_node is None:
                return False
            else:
                current_node = current_node.next_node

    def remove(self, data):
        current_node: Node = self.root
        while current_node is not None:
            if current_node.data == data:
                if current_node.previous_node is not None:
                    if current_node.next_node is not None:
                        current_node.next_node.previous_node = current_node.next_node
                        current_node.previous_node.next_node = current_node.previous_node
                    else:
                        current_node.previous_node.next_node = None
                        self.last = current_node.previous_node
                else:
                    self.root = current_node.next_node
                    current_node.next_node.previous_node = self.root
                self.size -= 1
                return True
            else:
                current_node = current_node.next_node
        return False

    def print_list(self):
        if self.root is None:
            return
        current_node = self.root
        print(current_node, end=" -> ")
        while current_node.next_node is not None:
            current_node = current_node.next_node
            print(current_node, end=" -> ")
        print()
