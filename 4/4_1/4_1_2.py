class Thing:
    __id=-1
    def __init__ (self,name, price):
        # self.id=self.__id
        self.name=name
        self.price=price
        self.weight, self.dims, self.memory, self.frm=None,None,None,None

    @classmethod
    def id_plus(cls):
        cls.__id+=1

    @classmethod
    def get_id(cls):
        return cls.__id


class Table(Thing):
    def __new__(cls, *args, **kwargs):
        Thing.id_plus()
        return super().__new__(cls)
    def __init__(self,name, price, weight, dims):
        super().__init__(name, price)
        self.id=Thing.get_id()
        self.weight, self.dims=weight,dims

class ElBook(Thing):
    def __new__(cls, *args, **kwargs):
        Thing.id_plus()
        return super().__new__(cls)
    def __init__(self,name, price, memory, frm):
        super().__init__(name, price)
        self.id=Thing.get_id()
        self.memory, self.frm=memory, frm

cl1_thing=Table("Круглый", 1024, 812.55, (700, 750, 700))
cl2_thing=Table("Прямоугол", 2, 3, (1, 2, 3))
cl3_thing=ElBook("Лук", 4, 5, (5, 6, 7))

print(cl1_thing.id)
print(Thing.get_id())
print(cl2_thing.id)
print(Thing.get_id())
print(cl3_thing.id)