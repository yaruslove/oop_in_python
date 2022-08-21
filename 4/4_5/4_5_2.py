class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __cls_id=-1
    def __new__(cls, *args, **kwargs):
        cls.__cls_id+=1
        return super().__new__(cls)
    def __init__ (self, name, weight, price):
        self._name=name
        self._weight=weight
        self._price=price
        self.__id=self.__cls_id
    def get_id(self):
        return self.__id


### Test

l=[ ShopItem('1','2',3),
    ShopItem('1','2',3),
    ShopItem('1','2',3),
    ShopItem('1','2',3)]

for i in l:
    print(i.get_id())
