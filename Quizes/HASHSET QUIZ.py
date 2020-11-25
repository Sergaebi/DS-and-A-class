class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:

    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        return hash(element) % self._capacity
        # return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, value):
        for element in self._hashtable:
            if element is not None:
                if element.value == value:
                    return element.key

    # This function should remove the entry with specified key and return the value. In case if the key does not exist, None should be returned.
    def remove(self, key):
        index = self._hash(key)
        while self._hashtable[index] is not None:
            if self._hashtable[index].key == key:
                break
            index = self._hash(index + 1)
        if self._hashtable[index] is None:
            return
        else:
            del self._hashtable[index]

    def size(self):
        return self._size

    # def print(self):
    #     print("printing hashset elements")
    #     for e in self._hashtable:
    #         while e is not None:
    #             print(e.value)
    #             e = e.next

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break

        return self._hashtable[tmpInd].value


class Node:

    def __init__(self, data, next_element=None):
        self.data = data
        self.next = next_element

    def __repr__(self):
        string = ""
        node = self
        while node is not None:
            string += (str(node.data) + " -> ")
            node = node.next
        return string


class HashSet:

    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def levelOrderIterator(self):
        for i in range(self._size):
            isYield = False
            for e in self._hashtable:
                for j in range(i):
                    if e is not None:
                        e = e.next
                if e is not None:
                    yield e.data
                    isYield = True
            if not isYield:
                break

    # def levelOrderIteratorWithQueue(self):
    #     yield None

    def _hash(self, element):
        return hash(element) % self._capacity
        # return ord(element[0]) % self._capacity

    def add(self, element):
        index = self._hash(element)
        if self._hashtable[index] is None:
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1

    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while n is not None:
            if n.data == element:
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        p = None
        while n is not None:
            if n.data == element:
                if p is None:
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self._size

    def union(self, s):
        newSet = HashSet(self._size + s.get_size())
        for element in self:
            newSet.add(element)
        for element in s:
            newSet.add(element)
        return newSet

    def union_update(self, s):
        newSet = self.union(s)
        print(newSet)
        for element in self:
            self.remove(element)
        for element in newSet:
            self.add(element)

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while e is not None:
                print(e.data)
                e = e.next

    def __iter__(self):
        for e in self._hashtable:
            if e is not None:
                self._elem = e
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
            for i in range(index + 1, len(self._hashtable)):
                if self._hashtable[i] is not None:
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def __str__(self):
        return str(self._hashtable)


def testing_union():
    HS1 = HashSet(5)

    HS1.add(10)
    HS1.add(40)
    HS1.add(13)
    HS1.add(17)

    HS2 = HashSet(5)

    HS2.add(140)
    HS2.add(43)
    HS2.add(131)
    HS2.add(173)

    print(HS1)
    print(HS2)
    final = HS1.union(HS2)
    print(final)
    list_to_check = []
    for element in final:
        list_to_check.append(element)
    if list_to_check == [40, 17, 10, 43, 131, 140, 173, 13]:
        print("UNION TEST PASSED\n")
    else:
        print("UNION TEST FAILED\n")


def testing_remove():
    H = HashMap()
    H.put(3, 4)
    H.put(4, 3)
    H.put(5, 6)
    H.put(2, 7)
    for element in H:
        print(element, end=" ")
    H.remove(3)
    print("\nRemoving 3")
    for element in H:
        print(element, end=" ")
    print("\nREMOVING FROM HASHSET: PASSED\n")

    if H.hasKey(3) == 4:
        print("HAS KEY: PASSED")
    else:
        print("HAS KEY: FAILED")


testing_union()
testing_remove()
