class Node:

    def __init__(self, data, next_level=None):
        self.data = data
        self.next = next_level

    def __repr__(self):
        string = ""
        node = self
        while node is not None:
            string += (str(node.data) + " -> ")
            node = node.next
        return string


class HashSet:

    def __init__(self, capacity):
        self.hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def _hash(self, element):
        return hash(element) % self._capacity

    def add(self, element):
        print(f"Adding {element}...")
        index = self._hash(element)
        if self.hashtable[index] is None:
            self.hashtable[index] = Node(element)
        else:
            n = Node(element, self.hashtable[index])
            self.hashtable[index] = n
        self._size += 1

    def contains(self, element):
        print(f"Checking if {element} in hashset...")
        index = self._hash(element)
        n = self.hashtable[index]
        while n is not None:
            if n.data == element:
                return True
            n = n.next
        return False

    def remove(self, element):
        print(f"Deleting {element}...")
        index = self._hash(element)
        n = self.hashtable[index]
        p = None
        while n is not None:
            if n.data == element:
                if p is None:
                    self.hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def get_size(self):
        return self._size

    def __iter__(self):
        for element in self.hashtable:
            if element is not None:
                self._elem = element
                break
        return self

    def __next__(self):
        if self._elem is None:
            raise StopIteration
        tmp = self._elem
        if self._elem.next is not None:
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self.hashtable)):
                if self.hashtable[i] is not None:
                    self._elem = self.hashtable[i]
                    break
        return tmp.data

    def __str__(self):
        return str(self.hashtable)


def main_testing():
    """Testing all functions of HashSet class"""
    print("Testing HashSet class methods...\n")

    # testing add function
    hashset = HashSet(10)
    hashset.add(10)
    hashset.add(30)
    hashset.add(13)
    print()
    print(hashset)
    if hashset.hashtable[0].data == 30 and hashset.hashtable[0].next.data == 10 and hashset.hashtable[3].data == 13:
        print("Testing add function: PASS\n")
    else:
        print("Testing add function: FAIL\n")

    # testing remove function
    hashset.remove(10)
    hashset.remove(13)
    print()
    print(hashset)
    if hashset.hashtable[0].next is None and hashset.hashtable[3] is None:
        print("Testing remove function: PASS\n")
    else:
        print("Testing remove function: FAIL\n")

    # testing contains function
    print(hashset)
    if hashset.contains(30) and not hashset.contains(10):
        print("Testing contains function: PASS\n")
    else:
        print("Testing contains function: FAIL\n")

    # testing contains function
    print(hashset)
    if hashset.get_size() == 1:
        print("Testing get_size function: PASS\n")
    else:
        print("Testing get_size function: FAIL\n")

    # testing __iter__ function
    hashset.add(32)
    hashset.add(45)
    hashset.add(55)
    hashset.add(41)
    hashset.add(321)
    hashset.add(629)
    print()
    print(hashset)
    list_to_check = []
    for item in hashset:
        list_to_check.append(item)
    print(f"With for loop appending items to list...\nFinal result = {list_to_check}")
    if list_to_check == [30, 321, 41, 32, 55, 45, 629]:
        print("Testing __iter__ function: PASS\n")
    else:
        print("Testing __iter__ function: FAIL\n")


if __name__ == '__main__':
    main_testing()
