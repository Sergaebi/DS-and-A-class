class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        if isinstance(self.value, bool):
            return f"{self.key}: bool {self.value}"
        elif isinstance(self.value, str):
            return f"{self.key}: str {self.value}"
        return f"{self.key}: int {self.value}"


class HashTable:

    def __init__(self):
        self.size = 16
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        multiplayer = 1
        hash_value = 0
        for character in key:
            hash_value += multiplayer * ord(character)
            multiplayer += 1
        return hash_value % self.size

    def put(self, key, value):
        print(f"Putting {value} at key: {key}...")
        item = HashItem(key, value)
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + 1) % self.size
        if self.slots[hash_value] is None:
            self.count += 1
        self.slots[hash_value] = item

    def get(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + 1) % self.size
        return None

    def remove(self, key):
        print(f"Removing at key: {key}...")
        index = self._hash(key)
        while self.slots[index] is not None:
            if self.slots[index].key == key:
                break
            index = self._hash(index + 1)
        if self.slots[index] is None:
            return
        else:
            del self.slots[index]

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __repr__(self):
        return str(self.slots)


def main_testing():
    """Testing all functions of HashTable class"""
    print("Testing HashTable class methods...\n")

    hashtable = HashTable()

    # testing put function
    hashtable.put("3", 3)
    hashtable.put("2", 2)
    hashtable.put("1", "1")
    hashtable.put("1300", True)
    print()
    print(hashtable)
    if hashtable.slots[1].value == "1" and hashtable.slots[2].value == 2:
        print("Testing put method: PASS\n")
    else:
        print("Testing put method: FAIL\n")

    # testing remove function
    hashtable.remove("3")
    hashtable.remove("1")
    print()
    print(hashtable)
    if hashtable["1"] is None and hashtable["3"] is None:
        print("Testing put method: PASS\n")
    else:
        print("Testing put method: FAIL\n")

    print("Methods __getitem__, __setitem__, and get are tested since methods put and remove use them...")


if __name__ == '__main__':
    main_testing()
