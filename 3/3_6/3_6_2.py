from typing import Union
import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))

class ShopItem:
    def __init__ (self,name, weight, price):
        self.name: str =name
        self.weight: Union[int,float] = ShopItem.check_numb(weight)
        self.price: Union[int,float] = ShopItem.check_numb(price)

    @staticmethod
    def check_numb(NumberString):
        if isinstance(NumberString,str):
            if NumberString.isdigit():
                Number = int(NumberString)
            else:
                Number = float(NumberString)
            return Number
        return NumberString


    def __hash__ (self):
        return hash((self.name.lower(),self.weight,self.price))

    def __eq__ (self,v):
        return hash(self)==hash(v)

    def __repr__ (self):
        return self.name


o1=ShopItem("Монитор Samsung:", "2000", "34000")
o2=ShopItem("Монитор Samsung:", "2000", "34000")
print(hash(o1))
print(hash(o2))
print("hash(o2)==hash(o1)",hash(o2)==hash(o1))
print(o2==o1)
# lst_in = list(map(str.strip, sys.stdin.readlines()))

a={}
a[o1]=1
a[o2]=2
print("a",a)

lst_in=["Системный блок: 1500 75890.56",
"Монитор Samsung: 2000 34000",
"Клавиатура: 200.44 545",
"Монитор Samsung: 2000 34000"]

shop_items=dict()
for i in lst_in:
    name=i.split(": ")[0]
    weight, price =i[len(name)+2:].split(" ")
    name+=":"
    tmp_obj=ShopItem(name, weight, price)
    if tmp_obj in shop_items:

        shop_items[tmp_obj][1]+=1
    else:
        shop_items[tmp_obj]=[tmp_obj,1]

print(shop_items)



