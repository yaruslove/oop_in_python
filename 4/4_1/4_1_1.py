class Animal:
    def __init__ (self,name, old):
        self.name=name
        self.old=old

    def get_info (self):
        lst_atr = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        lst_atr.remove("name")
        lst_atr.remove("old")
        part_return=str()
        for name_atr in lst_atr:
            part_return = f"{part_return}{getattr(self, name_atr)}, " 

        return f"{self.name}: {self.old}, {part_return[:-2]}"

class Cat(Animal):
    def __init__ (self,name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__ (self,name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

cat = Cat('кот', 4, 'black', 2.25)
# print(cat.get_info())
print(cat.get_info())
        