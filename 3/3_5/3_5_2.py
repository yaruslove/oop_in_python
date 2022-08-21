import operator

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    def __init__ (self, a, b, c):
        self.__a=a
        self.__b=b
        self.__c=c
        self.volume=self.__a * self.__b * self.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self,val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__a=val
            self.update_volume()

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self,val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__b=val
            self.update_volume()

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self,val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__c=val
            self.update_volume()

    def update_volume (self):
        self.volume=self.__a * self.__b * self.__c

    def __lt__ (self, value):
        return self.volume < value.volume

    def __le__ (self, value):
        return self.volume <= value.volume

class ShopItem:
    def __init__ (self,name, price, dim):
        self.name, self.price, self.dim=name, price, dim

ked_d=Dimensions(40, 30, 120)
ked=ShopItem("кеды", 1024,ked_d)

zont_d=Dimensions(10, 20, 50)
zont=ShopItem("зонт", 500.24,zont_d)

hol_d=Dimensions(2000, 600, 500)
hol=ShopItem("холодильник", 40000,hol_d)

tab_d=Dimensions(500, 200, 200)
tab=ShopItem("табуретка", 2000.99, tab_d)

lst_shop=[ked,zont,hol,tab]
print(lst_shop)

[print(i.name) for i in lst_shop]
[print(i.dim.volume) for i in lst_shop]

# def take_sort(elem):
#     return elem.dim.volume


lst_shop_sorted = sorted(lst_shop, key=operator.attrgetter('dim'))

# lst_shop_sorted = sorted(lst_shop, key="dim")
print("")
print([i.name for i in lst_shop_sorted])
print("")
print([i.name for i in lst_shop])


print("")
print(lst_shop_sorted[-1].name)
print(lst_shop_sorted[0].dim<lst_shop_sorted[1].dim<lst_shop_sorted[2].dim<lst_shop_sorted[3].dim)
print("")
print("Posle")
print(lst_shop_sorted[3].dim.c)
print(lst_shop_sorted[3].dim.volume)
lst_shop_sorted[3].dim.c=9
print("")
print(lst_shop_sorted[3].dim.c)
print(lst_shop_sorted[3].dim.volume)