class BinarySearchTree:

    def __init__(self, data_root, left_child=None, right_child=None):
        self.data = data_root
        self.left_child: BinarySearchTree = left_child
        self.right_child: BinarySearchTree = right_child

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left_child is not None:
                return self.left_child.insert(data)
            else:
                self.left_child = BinarySearchTree(data)
                return True
        else:
            if self.right_child is not None:
                return self.right_child.insert(data)
            else:
                self.right_child = BinarySearchTree(data)
                return True

    def find(self, data):
        if self.data == data:
            return self.data
        elif self.data > data:
            if self.left_child is None:
                return False
            else:
                self.left_child.find(data)
        elif self.data < data:
            if self.right_child is None:
                return False
            else:
                self.right_child.find(data)

    def __len__(self):
        if self.left_child is not None and self.right_child is not None:
            return 1 + self.left_child.__len__() + self.right_child.__len__()
        elif self.left_child:
            return 1 + self.left_child.__len__()
        elif self.right_child:
            return 1 + self.right_child.__len__()
        else:
            return 1

    def preorder_traversal(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left_child:
                self.left_child.preorder_traversal()
            if self.right_child:
                self.right_child.preorder_traversal()

    def inorder_traversal(self):
        if self is not None:
            if self.left_child:
                self.left_child.inorder_traversal()
            print(self.data, end=" ")
            if self.right_child:
                self.right_child.inorder_traversal()