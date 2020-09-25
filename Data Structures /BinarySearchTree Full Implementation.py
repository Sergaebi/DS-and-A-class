class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None



class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.array = []

    def insert_data(self, *args):
        removed_duplicates = []
        [removed_duplicates.append(x) for x in args if x not in removed_duplicates]
        for data in removed_duplicates:
            if self.root is None:
                self.root = Node(data)
            else:
                self.__insert_node(data, self.root)

    def __insert_node(self, data, node: Node):
        if data < node.data:
            if node.left_child is not None:
                self.__insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child is not None:
                self.__insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def __remove_node(self, data, node: Node):
        if node is None:
            return node
        elif data < node.data:
            node.left_child = self.__remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.__remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("Removing a leaf node...")
                del node
                return None
            elif not node.left_child:
                print("Removing a node with single right child...")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print('Removing a node with a single left child...')
                temp_node = node.left_child
                del node
                return temp_node
            elif node.left_child and node.right_child:
                print("Removing a node with two children...")
                temp_node = self.get_predecessor(node.left_child)
                node.data = temp_node.data
                node.left_child = self.__remove_node(temp_node.data, node.left_child)
        return node

    def remove(self, data):
        if self.root:
            self.root = self.__remove_node(data, self.root)

    def get_predecessor(self, node: Node):
        if node.right_child is not None:
            return self.get_predecessor(node.right_child)
        else:
            return node

    def __get_min(self, node: Node):
        if node.left_child:
            return self.__get_min(node.left_child)
        else:
            return node.data

    def get_min_value(self):
        if self.root:
            return self.__get_min(self.root)

    def __get_max(self, node: Node):
        if node.right_child:
            return self.__get_max(node.right_child)
        else:
            return node.data

    def get_max_value(self):
        if self.root:
            return self.__get_max(self.root)

    def __traverse_in_order(self, node: Node):
        if node.left_child:
            self.__traverse_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            self.__traverse_in_order(node.right_child)

    def traverse(self):
        if self.root:
            return self.__traverse_in_order(self.root)

    def __store_to_list(self, node: Node):
        self.array.append(node.data)
        if node.left_child:
            self.__store_to_list(node.left_child)
        if node.right_child:
            self.__store_to_list(node.right_child)

    def store_to_list(self):
        if self.root:
            return self.__store_to_list(self.root)

    def __get_height(self, node: Node):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left_child), self.__get_height(node.right_child))

    def get_height(self):
        if self.root:
            return self.__get_height(self.root)

    def __len__(self):
        self.store_to_list()
        return len(self.array)

    def __repr__(self):
        lines = self._build_tree_string(self.root, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    @classmethod
    def _build_tree_string(cls, root: Node, curr_index, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data)
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = \
            cls._build_tree_string(root.left_child, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            cls._build_tree_string(root.right_child, 2 * curr_index + 2, index, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0
        line1.append(node_repr)
        line2.append(' ' * new_root_width)
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)
        return new_box, len(new_box[0]), new_root_start, new_root_end


tree = BinarySearchTree()
