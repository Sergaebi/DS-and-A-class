class Queue:

    def __init__(self) -> None:
        self.items: list = []

    def enqueue(self, data):
        print(f"Adding {data}...")
        self.items.append(data)

    def dequeue(self):
        print(f"Removing element...")
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return None

    def __repr__(self):
        return str(self.items)


def main_testing():
    """Testing all functions of Queue class"""
    print("Testing Queue class methods...\n")

    # testing enqueue function
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print()
    print(queue)
    if queue.items == [2, 3, 4]:
        print("Testing enqueue function: PASS\n")
    else:
        print("Testing enqueue function: FAIL\n")

    # testing dequeue function
    queue.dequeue()
    queue.dequeue()
    print()
    print(queue)
    if queue.items == [4]:
        print("Testing dequeue function: PASS\n")
    else:
        print("Testing dequeue function: FAIL\n")


if __name__ == '__main__':
    main_testing()
