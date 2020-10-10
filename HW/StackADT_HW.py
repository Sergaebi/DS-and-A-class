from abc import ABC, abstractmethod


class StackADT(ABC):

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def get_top(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    def get_size(self):
        pass


class StackList(StackADT):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class StackLinkedList(StackADT):

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, data):
        new_node = Node(data)
        if self.__top:
            new_node.next_node = self.__top
            self.__top = new_node
        else:
            self.__top = new_node

    def pop(self):
        if self.__top:
            data = self.__top.data
            self.__size -= 1
            if self.__top.next_node:
                self.__top = self.__top.next_node
            else:
                self.__top = None
            return data
        else:
            return None

    def get_top(self):
        if self.__top:
            return self.__top.data
        return None

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False


def infixToPostfix(infix_expression):
    precedence = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    op_stack = StackList()
    postfix_list = []
    token_list = infix_expression.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (precedence[op_stack.get_top()] >= precedence[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
