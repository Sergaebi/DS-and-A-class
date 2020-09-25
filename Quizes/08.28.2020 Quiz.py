class Item:

    def __init__(self, volume: float, weight: float, name: str) -> None:
        self.volume = volume
        self.weight = weight
        self.name = name

    def __str__(self) -> str:
        return self.name


class Bag:

    def __init__(self, max_volume: float, max_weight: float, material: str = None) -> None:
        # self.material = material
        self.containing: list = []
        self.__max_weight = max_weight
        self.__max_volume = max_volume
        self.volume_inside: int = 0
        self.weight_inside: int = 0

    def put_in(self, item: Item) -> None:
        if (self.weight_inside + item.weight > self.__max_weight) or self.volume_inside + item.volume > self.__max_volume:
            print("Bag is not that big!")
        else:
            self.volume_inside += item.volume
            self.weight_inside += item.weight
            self.containing.append(item)

    def take_out(self, item: Item) -> None:
        if item in self.containing:
            self.weight_inside -= item.weight
            self.volume_inside -= item.volume
            self.containing.remove(item)
        else:
            print("No such item in box")

    def __repr__(self) -> str:
        if len(self.containing) == 0:
            return "Box contains nothing"
        return "Box contains: {}".format(", ".join(str(item) for item in self.containing))
