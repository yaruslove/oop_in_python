class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id

class ShopGenericView:
    def __repr__ (self):
        retrn=str()
        for k,v in self.__dict__.items():
            retrn=f"{retrn}\n{k}: {v}"
        return retrn.strip()

class ShopUserView:
    def __repr__ (self):
        retrn=str()
        for k,v in self.__dict__.items():
            if k=="_id":
                continue
            retrn=f"{retrn}\n{k}: {v}"
        return retrn.strip()

class Book(ShopItem,ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

book = Book("Python ООП", "Балакирев", 2022)
print(book)

