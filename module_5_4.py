class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        return self.name

    def go_to(self, new_floor):
        n = 0
        if new_floor > self.number_of_floors or new_floor > 1:
            for i in range(new_floor):
                n += 1
                print(n)
        else:
            print("Такого этажа не существует")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


Home1 = House('Склад', 10)
print(House.houses_history)
Home2 = House('Офис', 20)
print(House.houses_history)
Home3 = House('Башня', 17)
print(House.houses_history)

del Home2
del Home3

print(House.houses_history)
