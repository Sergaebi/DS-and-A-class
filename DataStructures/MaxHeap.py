class MaxHeap:

    def __init__(self, items=None):
        self.heap = [0]
        if items is not None:
            for item in items:
                self.heap.append(item)
                self.__move_up(len(self.heap) - 1)

    def pop_max(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            maximum = self.heap.pop()
            self.__move_down(1)
        elif len(self.heap) == 2:
            maximum = self.heap.pop()
        else:
            maximum = False
        return maximum

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __move_up(self, index_to_swap):
        parent_index = index_to_swap // 2
        if parent_index <= 1:
            return
        elif self.heap[parent_index] < self.heap[index_to_swap]:
            self.__swap(index_to_swap, parent_index)
            self.__move_up(parent_index)

    def __move_down(self, index_to_swap):
        left_child = index_to_swap * 2
        right_child = index_to_swap * 2 + 1
        largest = index_to_swap
        if len(self.heap) > left_child and self.heap[largest] < self.heap[left_child]:
            largest = left_child
        if len(self.heap) > right_child and self.heap[largest] < self.heap[right_child]:
            largest = right_child
        if largest != index_to_swap:
            self.__swap(index_to_swap, largest)
            self.__move_up(largest)

    def __repr__(self):
        return self.heap
