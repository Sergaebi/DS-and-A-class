class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    def insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.data:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)
        if balance > 1 and key < node.left.data:
            return self.rightRotate(node)
        if balance < -1 and key > node.right.data:
            return self.leftRotate(node)
        if balance > 1 and key > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and key < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def delete(self, node, key):
        if not node:
            return node
        elif key < node.val:
            node.left = self.delete(node.left, key)
        elif key > node.val:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp
            temp = self.getMinValueNode(node.right)
            node.val = temp.val
            node.right = self.delete(node.right, temp.val)
        if node is None:
            return node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        balance = self.getBalance(node)
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    @staticmethod
    def getHeight(node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def preOrder(self, node):
        if not node:
            return
        print("{} ".format(node.data), end="")
        self.preOrder(node.left)
        self.preOrder(node.right)


myTree = AVLTree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = myTree.insert(root, num)

print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()
_key = 10
root = myTree.delete(root, _key)
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
print()
