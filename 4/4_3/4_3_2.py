class Thing:
    def __init__ (self,name, weight):
        self.name, self.weight = name, weight


class ArtObject(Thing):
    def __init__ (self, name, weight, author, date):
        super().__init__(name, weight)
        self.author, self.date = author, date

class Computer(Thing):
    def __init__ (self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory, self.cpu = memory, cpu

class Auto(Thing):
    def __init__ (self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self,name, weight, dims, model, old): # model - модель (строка); old - время использования, в годах (целое число)
        super().__init__(name, weight,dims)
        self.model = model
        self.old = old

class Toyota(Auto):
    def __init__(self,name, weight, dims, model, wheel): # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel
