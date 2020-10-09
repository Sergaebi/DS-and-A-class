# Python code to delete a node in AVL tree
# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports insertion,
# deletion operations
class AVLTree(object):

    def insert(self, node, key):

        # Step 1 - Perform normal BST
        if not node:
            return TreeNode(key)
        elif key < node.val:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < node.left.val:
            return self.rightRotate(node)

        # Case 2 - Right Right
        if balance < -1 and key > node.right.val:
            return self.leftRotate(node)

        # Case 3 - Left Right
        if balance > 1 and key > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4 - Right Left
        if balance < -1 and key < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, node, key):

        # Step 1 - Perform standard BST delete
        if not node:
            return node

        elif key < node.val:
            node.left = self.delete(node.left, key)

        elif key > node.val:
            node.right = self.delete(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.getMinValueNode(node.right)
            node.val = temp.val
            node.right = self.delete(node.right,
                                     temp.val)

        # If the tree has only one node,
        # simply return it
        if node is None:
            return node

        # Step 2 - Update the height of the
        # ancestor node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
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

        print("{0} ".format(node.val), end="")
        self.preOrder(node.left)
        self.preOrder(node.right)


myTree = AVLTree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = myTree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()

# Delete
key = 10
root = myTree.delete(root, key)

# Preorder Traversal
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
print()

# This code is contributed by Ajitesh Pathak
