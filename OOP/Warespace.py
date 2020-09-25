class Material:

    def __init__(self, material_type, amount):

        if material_type == "Iron":
            self.max_capacity = 30
        elif material_type == "Copper":
            self.max_capacity = 40
        elif material_type == "Gold":
            self.max_capacity = 50

        if amount > self.max_capacity:
            raise ValueError("Amount is more than the max capacity of this material type")

        self.amount = amount
        self.material_type = material_type
        self.material_with_its_amount = [self.material_type, self.amount]

    def __str__(self):
        return "{} of {}".format(self.material_with_its_amount[1], self.material_with_its_amount[0])


class Warehouse:

    def __init__(self):
        self.__items_inside = []

    def get_space(self):
        return 20 - len(self.__items_inside)

    def put_in(self, item: Material):

        if len(self.__items_inside) > 20:
            print("Warehouse is full")

        else:
            for material in self.__items_inside:
                if item.material_type == material.material_type:
                    sum_to_check = material.amount + item.material_with_its_amount[1]
                    if sum_to_check > item.max_capacity:
                        print(f"{item.material_type} {item.max_capacity} max border passed")
                        print(f"Overwriting existing {item.material_type}")
                        self.__items_inside[self.__items_inside.index(material)] = item
                        return
                    material.material_with_its_amount[1] += item.material_with_its_amount[1]
                    return
            self.__items_inside.append(item)

    def remove(self, item: Material):

        if len(self.__items_inside) == 0:
            print("There is nothing inside")

        else:
            try:
                self.__items_inside.remove(item)
            except ValueError:
                print("No such item inside warehouse")

    def __repr__(self):
        return "; ".join(str(x) for x in self.__items_inside)
