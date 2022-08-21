class Book:
    def __init__(self,title, author, year):
        self.title=title
        self.author=author
        self.year=year



class Lib:
    def __init__(self) -> None:
        self.book_list=list()

    def __add__ (self, bk):
        self.book_list.append(bk)
        return self

    def __iadd__ (self,bk):
        self.book_list.append(bk)
        return self

    def __sub__ (self, bk):
        if isinstance(bk ,Book) and self.book_list:
            cp_lst=self.book_list.copy()
            for chkb in cp_lst:
                if chkb==bk:
                    self.book_list.remove(bk)
                    return self
        elif isinstance(bk ,int) and len(self.book_list)>=bk+1:
            del self.book_list[bk]
            return self
        else:
            return self

    def __isub__ (self,bk):
        if isinstance(bk ,Book) and self.book_list:
            cp_lst=self.book_list.copy()
            for chkb in cp_lst:
                if chkb==bk:
                    self.book_list.remove(bk)
                    return self
        elif isinstance(bk ,int) and len(self.book_list)>=bk+1:
            del self.book_list[bk]
            return self
        else:
            return self

    def __len__ (self):
        return len(self.book_list)


book1 = Book("title1", "author1", "year1")
book2 = Book("title2", "author2", "year2")
book3 = Book("title3", "author3", "year3")


lib = Lib()
lib = lib + book1
lib += book2
lib = lib + book3

for i in lib.book_list:
    print(i.title)

print("\n")

lib -=  2

for i in lib.book_list:
    print(i.title)




    

        
