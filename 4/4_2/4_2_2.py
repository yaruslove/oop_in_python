class Thing:
    def __init__ (self,name, price, weight):
        self.name, self.price, self.weight =name, price, weight

    def __hash__ (self):
        return hash ((self.name,self.price,self.weight))

    
class DictShop(dict):
    def __init__(self, dct=None):
        if dct == None:
            dct={}
        if type(dct)!=dict:
            raise TypeError('аргумент должен быть словарем')
        if dct!={} and not all([isinstance(key,Thing) for key in dct]):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return super().__init__(dct)

    def __setitem__(self,key,value):
        if not isinstance(key,Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key,value)

    