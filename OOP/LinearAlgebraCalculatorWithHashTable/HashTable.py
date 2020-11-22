class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class HashTable:

    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        return hash(element) % self._capacity

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

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break
        return self

    def __next__(self):
        try:
            if self._index >= len(self._hashtable):
                raise StopIteration
            tmpInd = self._index
            self._index = len(self._hashtable)
            for i in range(tmpInd + 1, len(self._hashtable)):
                if self._hashtable[i] is not None:
                    self._index = i
                    break
            return self._hashtable[tmpInd]
        except AttributeError:
            pass

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def items(self):
        new_list = []
        for i in self:
            entry = (i.key, i.value)
            new_list.append(entry)
        return new_list

    def __repr__(self):
        return str(self._hashtable)
