class SellItem:
    def __init__ (self, name, price):
        self.name, self.price =  name, price


class House(SellItem):
    def __init__ (self, name, price,material, square):
        super().__init__(name, price)
        self.material, self.square =  material, square


class Flat(SellItem):
    def __init__ (self, name, price,size, rooms):
        super().__init__(name, price)
        self.size, self.rooms=size, rooms

class Land(SellItem):
    def __init__ (self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__ (self,name):
        self.name=name
        self.lst=[]

    def add_object(self,obj):
        self.lst.append(obj)

    def remove_object(self,obj):
        self.lst.remove(obj)

    def get_objects(self):
        return self.lst
        