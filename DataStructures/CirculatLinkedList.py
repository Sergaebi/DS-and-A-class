class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node: Node = next_node

    def __repr__(self):
        return str(self.data)


class CircularLinkedList:

    def __init__(self, root=None):
        self.root: Node = root
        self.size = 0

    def add_beginning(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, data):
        current_node = self.root
        while True:
            if current_node.data == data:
                return current_node, data
            elif current_node.next_node == self.root:
                return False
            current_node = current_node.next_node

    def remove(self, data):
        current_node = self.root
        previous_node = None
        while True:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next_node = current_node.next_node
                else:
                    while current_node.next_node != self.root:
                        current_node = current_node.next_node
                    current_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif current_node.next_node == self.root:
                return False
            previous_node = current_node
            current_node = current_node.next_node

    def __repr__(self):
        if self.root is None:
            return
        current_node = self.root
        print(current_node, end=" -> ")
        while current_node.next_node != self.root:
            current_node = current_node.next_node
            print(current_node, end=" -> ")
        print()

    def __len__(self):
        return self.size
