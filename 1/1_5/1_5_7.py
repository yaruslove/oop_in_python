class Cart:
    def __init__(self):
        self.goods=[]
    def add(self,gd):
        self.goods.append(gd)
    def remove(self,indx):
        del self.goods[indx]
    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]

class Gds:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Table(Gds):
    pass
class TV(Gds):
    pass
class Notebook(Gds):
    pass
class Cup(Gds):
    pass

cart=Cart()
tv1=TV('lg',1000)
tv2=TV('sams',2000)
cart.add(tv1)
cart.add(tv2)


nt1=Notebook('asus',10000)
nt2=Notebook('acer',20000)
cart.add(nt1)
cart.add(nt2)

cp=Cup('mag',5)
tb=Table('hoff',40)
cart.add(cp)
cart.add(tb)


 